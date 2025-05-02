from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

@tool(name="monthlyPaymentCalc",
      description="Calculates the monthly repayment for a policy when provided with the policy premium and interest rate.",
      permission=ToolPermission.ADMIN)
def monthly_payment_calc(premium:float, rate:float):
    n =  12  # total number of months
    r = rate / (100 * 12)  # interest per month
    monthly_payment = premium * ((r * ((r + 1) ** n)) / (((r + 1) ** n) - 1))
    return monthly_payment



