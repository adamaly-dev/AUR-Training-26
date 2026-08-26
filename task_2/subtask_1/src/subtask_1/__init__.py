from pathlib import Path

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
                for key, value in stock_dict.items():
                    print(f"{key}: {value}")
                new_key = input("Enter a stock type: ").strip().lower()
                try:
                    new_value = int(input("Enter the stock value: ").strip())
                except:
                    raise ValueError("Stock value must be an integer")
                if new_key in stock_dict:
                    stock_dict[new_key] += new_value
                else:
                    stock_dict[new_key] = new_value
            elif query_type == 2:
                pass
            elif query_type == 3:
                pass
            elif query_type == 4:               
                pass         
            else:
                raise ValueError("Query type must be between (1-4)")
        except:
            raise TypeError("Query type must be an integer")

main()