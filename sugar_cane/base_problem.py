def calculate_profit(
    profit_per_sugar: float,
    sugar_produced: float,
    profit_per_etanol: float,
    etanol_produced: float    
):
    # max z = c1x1 + c2x2 
    z = (profit_per_sugar * sugar_produced) + (profit_per_etanol * etanol_produced)
    return z



if __name__ == "__main__":
    # c1
    profit_per_sugar_ton = 1.7
    # c2
    profit_per_etanol_1000l = 1.9
    # a11
    sugar_ton_need_sugar_cane_ton = 3
    # a12
    etanol_1000l_need_sugar_cane_ton = 2.5
    # S
    hectar = 200
    # k
    hectar_to_sugar_cane_ton = 7

    # total sugar cane = S * k
    total_sugar_cane = hectar *  hectar_to_sugar_cane_ton

    # total produced sugar = x1 = (S * k) / a11
    total_produced_sugar = total_sugar_cane / sugar_ton_need_sugar_cane_ton
    # total produced etanol = x2 = (S * k) / a12
    total_produced_etanol = total_sugar_cane / etanol_1000l_need_sugar_cane_ton

    # sugar_profit = c1 * x1
    sugar_profit = profit_per_sugar_ton * total_produced_sugar
    # etanol_profit = c1 * x2
    etanol_profit = profit_per_etanol_1000l * total_produced_etanol