TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print("Electricity bill estimator 2.0")
    tariff_type = input("Which tariff? 11 or 31:")
    if tariff_type == "11":
        price_per_kWh = TARIFF_11
    else:
        price_per_kWh = TARIFF_31

    daily_use_kWh = float(input("Enter daily use in kWh: "))

    number_of_days_billing_period = int(input("Enter number of billing days: "))

    estimated_bill = price_per_kWh * daily_use_kWh * number_of_days_billing_period
    print(f"Estimated bill: ${estimated_bill:.2f}")


main()
