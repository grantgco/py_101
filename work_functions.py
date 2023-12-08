def excess_cv_rate(total_excess_premium, total_revenue, contract_cv):
    # Returns the excess CV rate for a contract per $1000 of contract CV
    return ((total_excess_premium / total_revenue) * contract_cv) / 1000

def print_excess_cv_rate(total_excess_premium, total_revenue, contract_cv):
    # Returns the excess CV rate for a contract per $1000 of contract CV
    rate = ((total_excess_premium / total_revenue) * contract_cv) / 1000
    print("The excess CV rate is " + str(round(rate, 2)) + " per $1,000 of contract CV (rounded to 2 decimal places)")


print_excess_cv_rate(20000, 100000, 50000)