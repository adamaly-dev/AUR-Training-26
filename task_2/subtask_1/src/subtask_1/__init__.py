from pathlib import Path

def disp(stock_dict) -> None:
    for key, value in stock_dict.items():
        print(f"{key}: {value}")

def inp_number() -> int:
    try:
        new_value = int(input("Enter the stock value: ").strip())
    except:
        raise ValueError("Stock value must be a positive integer")
    if new_value <= 0:
        raise ValueError("Stock value must be a positive integer")
    return new_value

def main() -> None:
    stock_dict = {}

    try:
        file_path = Path(__file__).parent / "stock.txt"
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    key, value = line.split(',')
                    stock_dict[key] = int(value)
    except:
        raise FileNotFoundError("File not found")

    while True:
        try:
            query_type = int(input("Enter query type (1-4): ").strip())
            if query_type == 1:
                disp(stock_dict)

                new_key = input("Enter a stock type: ").strip().lower()
                new_value = inp_number()

                if new_key in stock_dict:
                    stock_dict[new_key] += new_value
                else:
                    stock_dict[new_key] = new_value
            elif query_type == 2:
                disp(stock_dict)

                new_key = input("Enter a stock type: ").strip().lower()
                if (new_key not in stock_dict):
                    raise ValueError("Stock doesn't exist")
                new_value = inp_number()

                if stock_dict[new_key] < new_value:
                    raise ValueError(f"Stock value to be removed is higher than the current stock value")
                stock_dict[new_key] -= new_value
            elif query_type == 3:
                disp(stock_dict)
            elif query_type == 4:               
                with open(file_path, "w") as f:
                    for key, value in stock_dict.items():
                        f.write(key+","+str(value)+"\n")
                break
            else:
                raise ValueError("Query type must be between (1-4)")
        except:
            raise TypeError("Query type must be an integer")

main()