from django.db import models
from .coverage import Coverage
from .policy import Policy


class PolicyCoverage(models.Model):
  
    policy_id = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name="policy_coverage")
    coverage_id = models.ForeignKey(Coverage, on_delete=models.CASCADE, related_name="policy_coverage")
