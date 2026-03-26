"""
Agent Evaluation Framework.

Provides a multi-dimensional evaluation system for assessing agent outputs
across configurable rubric dimensions with weighted scoring.

Use when:
 - Evaluating agent outputs against multi-dimensional rubrics
 - Building automated evaluation pipelines for agent systems
 - Monitoring production agent quality with sampling
 - Comparing agent configurations or model versions

Usage:
 from evaluator import AgentEvaluator, TestSet, EvaluationRunner

 evaluator = AgentEvaluator()
 result = evaluator.evaluate(output="Agent response text", ground_truth="Expected answer")
 print(f"Passed: {result['passed']}, Score: {result['overall_score']:.2f}")

 # Or run a full test set
 test_set = TestSet("my_tests")
 test_set.add_test({"name": "test1", "input": "query", "expected": {"answer": "Paris"}})
 runner = EvaluationRunner(test_set, DEFAULT_RUBRIC, my_agent)
 summary = runner.run_all(verbose=True)
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import time
import random

__all__ = [
    "ScoreLevel",
    "RubricDimension",
    "DEFAULT_RUBRIC",
    "AgentEvaluator",
    "TestSet",
    "EvaluationRunner",
    "ProductionMonitor",
]


# ============================================================================
# Score Levels
# ============================================================================


class ScoreLevel(Enum):
    """Qualitative score levels mapped to numeric values.

    Use when: converting qualitative assessments (excellent, good, etc.)
    to numeric scores for aggregation and comparison.
    """

    EXCELLENT = 1.0
    GOOD = 0.8
    ACCEPTABLE = 0.6
    POOR = 0.3
    FAILED = 0.0


# ============================================================================
# Rubric Definition
# ============================================================================


@dataclass
class RubricDimension:
    """A single evaluation dimension within a rubric.

    Use when: defining what to measure and how to weight it
    in a multi-dimensional evaluation rubric.
    """

    name: str
    weight: float
    description: str
    levels: Dict[str, float] = field(default_factory=lambda: {
        "excellent": 1.0,
        "good": 0.8,
        "acceptable": 0.6,
        "poor": 0.3,
        "failed": 0.0,
    })


DEFAULT_RUBRIC: Dict[str, RubricDimension] = {
    "factual_accuracy": RubricDimension(
        name="factual_accuracy",
        weight=0.30,
        description="Claims match ground truth",
    ),
    "completeness": RubricDimension(
        name="completeness",
        weight=0.25,
        description="All requested aspects covered",
    ),
    "tool_efficiency": RubricDimension(
        name="tool_efficiency",
        weight=0.20,
        description="Right tools used a reasonable number of times",
    ),
    "citation_accuracy": RubricDimension(
        name="citation_accuracy",
        weight=0.15,
        description="Citations match claimed sources",
    ),
    "source_quality": RubricDimension(
        name="source_quality",
        weight=0.10,
        description="Appropriate primary sources used",
    ),
}


# ============================================================================
# Evaluator
# ============================================================================


class AgentEvaluator:
    """Multi-dimensional agent output evaluator.

    Use when: scoring agent outputs against a rubric with per-dimension
    scores and a weighted overall score.
    """

    def __init__(
        self,
        rubric: Optional[Dict[str, RubricDimension]] = None,
        pass_threshold: float = 0.7,
    ) -> None:
        self.rubric = rubric or DEFAULT_RUBRIC
        self.pass_threshold = pass_threshold

    def evaluate(
        self,
        output: str,
        ground_truth: str = "",
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Evaluate an agent output against the rubric.

        Use when: scoring a single agent response. Returns per-dimension
        scores, weighted overall score, and pass/fail determination.

        In production, replace ``_score_dimension`` with LLM-as-judge
        or human evaluation for each dimension.
        """
        dimension_scores: Dict[str, float] = {}

        for name, dimension in self.rubric.items():
            score = self._score_dimension(output, ground_truth, dimension, context)
            dimension_scores[name] = score

        overall = self._weighted_average(dimension_scores)

        return {
            "overall_score": overall,
            "dimension_scores": dimension_scores,
            "passed": overall >= self.pass_threshold,
            "pass_threshold": self.pass_threshold,
        }

    def _score_dimension(
        self,
        output: str,
        ground_truth: str,
        dimension: RubricDimension,
        context: Optional[Dict[str, Any]] = None,
    ) -> float:
        """Score a single dimension.

        CUSTOMIZE: Replace this with LLM-as-judge evaluation or
        human scoring for production use. This placeholder returns
        a heuristic score based on output length.
        """
        # Placeholder heuristic — replace with real evaluation
        if not output:
            return 0.0
        if ground_truth and ground_truth.lower() in output.lower():
            return 1.0
        if len(output) > 100:
            return 0.8
        if len(output) > 20:
            return 0.6
        return 0.3

    def _weighted_average(self, dimension_scores: Dict[str, float]) -> float:
        """Calculate weighted average across dimensions."""
        total_weight = 0.0
        weighted_sum = 0.0

        for name, score in dimension_scores.items():
            if name in self.rubric:
                weight = self.rubric[name].weight
                weighted_sum += score * weight
                total_weight += weight

        return weighted_sum / total_weight if total_weight > 0 else 0.0


# ============================================================================
# Test Set
# ============================================================================


class TestSet:
    """Manages a collection of evaluation test cases.

    Use when: organizing test cases with tagging, filtering,
    and complexity stratification for systematic evaluation.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.tests: List[Dict[str, Any]] = []
        self.tags: Dict[str, List[int]] = {}

    def add_test(self, test_case: Dict[str, Any]) -> None:
        """Add a test case to the set."""
        self.tests.append(test_case)

        for tag in test_case.get("tags", []):
            if tag not in self.tags:
                self.tags[tag] = []
            self.tags[tag].append(len(self.tests) - 1)

    def filter(self, **criteria: Any) -> List[Dict[str, Any]]:
        """Filter tests by criteria (e.g., complexity='simple')."""
        filtered = []
        for test in self.tests:
            match = all(test.get(k) == v for k, v in criteria.items())
            if match:
                filtered.append(test)
        return filtered

    def get_complexity_distribution(self) -> Dict[str, int]:
        """Get count of tests per complexity level."""
        distribution: Dict[str, int] = {}
        for test in self.tests:
            complexity = test.get("complexity", "medium")
            distribution[complexity] = distribution.get(complexity, 0) + 1
        return distribution

    def get_by_tag(self, tag: str) -> List[Dict[str, Any]]:
        """Get all tests with a specific tag."""
        indices = self.tags.get(tag, [])
        return [self.tests[i] for i in indices]


# ============================================================================
# Evaluation Runner
# ============================================================================


class EvaluationRunner:
    """Orchestrates evaluation runs across a test set.

    Use when: running a full evaluation pass, collecting per-test results,
    and producing summary reports with per-dimension averages.
    """

    def __init__(
        self,
        test_set: TestSet,
        rubric: Dict[str, RubricDimension],
        agent: Any,
        pass_threshold: float = 0.7,
    ) -> None:
        self.test_set = test_set
        self.evaluator = AgentEvaluator(rubric, pass_threshold)
        self.agent = agent
        self.results: List[Dict[str, Any]] = []

    def run_all(self, verbose: bool = False) -> Dict[str, Any]:
        """Run evaluation on all tests in the set.

        Returns a summary dict with pass rate, dimension averages,
        and a list of failures.
        """
        self.results = []

        for i, test in enumerate(self.test_set.tests):
            if verbose:
                print(f"Running test {i + 1}/{len(self.test_set.tests)}: {test.get('name', 'unnamed')}")

            result = self._run_single(test)
            self.results.append(result)

        return self.summarize()

    def _run_single(self, test: Dict[str, Any]) -> Dict[str, Any]:
        """Run a single test case."""
        output = self.agent.run(test["input"])
        ground_truth = test.get("expected", {}).get("answer", "")

        evaluation = self.evaluator.evaluate(
            output=output,
            ground_truth=ground_truth,
            context=test,
        )

        return {
            "test": test,
            "output": output,
            "evaluation": evaluation,
        }

    def summarize(self) -> Dict[str, Any]:
        """Produce summary statistics from evaluation results."""
        if not self.results:
            return {"error": "No results"}

        passed = sum(1 for r in self.results if r["evaluation"]["passed"])

        # Per-dimension averages
        dimension_totals: Dict[str, Dict[str, float]] = {}
        for name in self.evaluator.rubric:
            dimension_totals[name] = {"total": 0.0, "count": 0}

        for result in self.results:
            for dim, score in result["evaluation"]["dimension_scores"].items():
                if dim in dimension_totals:
                    dimension_totals[dim]["total"] += score
                    dimension_totals[dim]["count"] += 1

        dimension_averages = {
            dim: data["total"] / data["count"]
            for dim, data in dimension_totals.items()
            if data["count"] > 0
        }

        return {
            "total_tests": len(self.results),
            "passed": passed,
            "failed": len(self.results) - passed,
            "pass_rate": passed / len(self.results),
            "dimension_averages": dimension_averages,
            "failures": [
                r for r in self.results if not r["evaluation"]["passed"]
            ],
        }


# ============================================================================
# Production Monitor
# ============================================================================


class ProductionMonitor:
    """Sampling-based quality monitor for deployed agents.

    Use when: monitoring live agent quality by evaluating a random
    sample of production interactions and alerting on degradation.
    """

    def __init__(self, sample_rate: float = 0.01) -> None:
        self.sample_rate = sample_rate
        self.samples: List[Dict[str, Any]] = []
        self.evaluator = AgentEvaluator()
        self.alert_thresholds = {
            "pass_rate_warning": 0.85,
            "pass_rate_critical": 0.70,
        }

    def sample_and_evaluate(
        self, query: str, output: str
    ) -> Optional[Dict[str, Any]]:
        """Evaluate a production interaction if selected by sampling.

        Returns evaluation dict if sampled, None otherwise.
        """
        if random.random() > self.sample_rate:
            return None

        evaluation = self.evaluator.evaluate(output=output)

        sample = {
            "query": query[:200],
            "output_preview": output[:200],
            "score": evaluation["overall_score"],
            "passed": evaluation["passed"],
            "timestamp": time.time(),
        }

        self.samples.append(sample)
        return sample

    def get_metrics(self) -> Dict[str, Any]:
        """Calculate current quality metrics from collected samples."""
        if not self.samples:
            return {"status": "insufficient_data"}

        passed = sum(1 for s in self.samples if s["passed"])
        pass_rate = passed / len(self.samples)
        avg_score = sum(s["score"] for s in self.samples) / len(self.samples)

        return {
            "sample_count": len(self.samples),
            "pass_rate": pass_rate,
            "average_score": avg_score,
            "status": self._get_status(pass_rate),
        }

    def _get_status(self, pass_rate: float) -> str:
        """Determine health status from pass rate."""
        if pass_rate < self.alert_thresholds["pass_rate_critical"]:
            return "critical"
        elif pass_rate < self.alert_thresholds["pass_rate_warning"]:
            return "warning"
        return "healthy"


# ============================================================================
# Demo / CLI entry point
# ============================================================================


if __name__ == "__main__":
    print("=== Agent Evaluation Framework Demo ===\n")

    # 1. Basic evaluation
    evaluator = AgentEvaluator()
    result = evaluator.evaluate(
        output="Paris is the capital of France, located along the Seine river.",
        ground_truth="Paris",
    )
    print(f"1. Basic eval: passed={result['passed']}, score={result['overall_score']:.2f}")
    for dim, score in result["dimension_scores"].items():
        print(f"   {dim}: {score:.2f}")

    # 2. Test set
    ts = TestSet("demo_tests")
    ts.add_test({
        "name": "capital_lookup",
        "input": "What is the capital of France?",
        "expected": {"answer": "Paris"},
        "complexity": "simple",
        "tags": ["geography", "factual"],
    })
    ts.add_test({
        "name": "comparison",
        "input": "Compare Python and JavaScript",
        "expected": {"answer": ""},
        "complexity": "medium",
        "tags": ["technical"],
    })
    print(f"\n2. Test set: {len(ts.tests)} tests")
    print(f"   Complexity distribution: {ts.get_complexity_distribution()}")
    print(f"   Tests tagged 'factual': {len(ts.get_by_tag('factual'))}")

    # 3. Production monitor
    monitor = ProductionMonitor(sample_rate=1.0)  # 100% for demo
    for i in range(20):
        monitor.sample_and_evaluate(
            query=f"Test query {i}",
            output=f"This is a sufficiently detailed response for query {i}. " * 3,
        )
    metrics = monitor.get_metrics()
    print(f"\n3. Production monitor: {metrics['sample_count']} samples")
    print(f"   Pass rate: {metrics['pass_rate']:.0%}")
    print(f"   Avg score: {metrics['average_score']:.2f}")
    print(f"   Status: {metrics['status']}")

    print("\n=== Demo Complete ===")
