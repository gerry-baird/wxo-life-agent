import random
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

@tool(name="lifeInterestRateLookup",
      description="This tool will determine the interest rate to be used when calculating monthly payments for life policies. The rate will be based on the value of the policy.",
      permission=ToolPermission.ADMIN)
def rate_lookup(value:float):
    rate = 15

    rate = random.randint(50, 100)
    rate = rate / 10
    return rate


