def get_first_item(data_list):
    """Returns the first item from a list."""
    return data_list[0] if data_list else None


"""
Get Dummies Explained 🚗
================================
This script shows how pd.get_dummies() works under the hood!

What is One-Hot Encoding?
--------------------------
Imagine you have car brands: Ford, Toyota, BMW
Computers can't understand words, only numbers.

So we turn each brand into its own column with 1 (True) or 0 (False):
- brand_Ford: Is it a Ford? 1 = Yes, 0 = No
- brand_Toyota: Is it a Toyota? 1 = Yes, 0 = No
- brand_BMW: Is it a BMW? 1 = Yes, 0 = No
"""
def get_dummies(data_list, column_name):
    """
    A beginner-friendly version of pd.get_dummies()
    
    Args:
        data_list: A list of values (like ['Ford', 'Toyota', 'BMW', 'Ford'])
        column_name: The name of the column (like 'brand')
    
    Returns:
        A dictionary with new columns
    """
    # STEP 1: Find all unique values (no duplicates)
    unique_values = []
    for item in data_list:
        if item not in unique_values:
            unique_values.append(item)
    
    print(f"Unique {column_name}s found: {unique_values}")
    print()
    
    # STEP 2: Create a new column for each unique value
    result = {}
    
    for unique_val in unique_values:
        # Create column name like "brand_Ford"
        new_column_name = f"{column_name}_{unique_val}"
        
        # For each item in original list, put 1 if it matches, 0 if not
        new_column = []
        for item in data_list:
            if item == unique_val:
                new_column.append(1)  # It's a match!
            else:
                new_column.append(0)  # Not a match
        
        result[new_column_name] = new_column
    
    return result


# ============================================
# LET'S TRY IT OUT! 🚀
# ============================================

if __name__ == "__main__":

    # Example: A list of car brands
    car_brands = ['Ford', 'Toyota', 'BMW', 'Ford', 'Toyota', 'Tesla', 'Mercedes', 'Chevrolet', 'Audi', 'Mercedes']
    
    print("=" * 50)
    print("ORIGINAL DATA")
    print("=" * 50)
    print(f"Car brands: {car_brands}")
    print()
    
    # Use our simple function
    print("=" * 50)
    print("AFTER ONE-HOT ENCODING (Our Simple Version)")
    print("=" * 50)
    encoded = get_dummies(car_brands, 'brand')
    
    # Print the results in a nice table format
    print(f"{'Index':<8}", end="")
    for col_name in encoded.keys():
        print(f"{col_name:<15}", end="")
    print()
    print("-" * 70)
    
    for i in range(len(car_brands)):
        print(f"{i:<8}", end="")
        for col_name in encoded.keys():
            print(f"{encoded[col_name][i]:<15}", end="")
        print()
    
    print()
    print("=" * 50)
    print("NOW LET'S COMPARE TO PANDAS get_dummies()")
    print("=" * 50)
    
    import pandas as pd
    
    # Create a DataFrame with our data
    df = pd.DataFrame({'brand': car_brands})
    print("Original DataFrame:")
    print(df)
    print()
    
    # Use pandas get_dummies
    df_encoded = pd.get_dummies(df, columns=['brand'])
    print("After pd.get_dummies():")
    print(df_encoded)
    print()
    
    print("✅ See? They produce the same result!")
    print("   pd.get_dummies() is just a faster, fancier version!")

    print()
    print("=" * 50)
    print("PERFORMANCE COMPARISON ⚡")
    print("=" * 50)
    
    import time
    
    # Create a larger dataset for fair comparison
    large_brands = car_brands * 10000000
    
    # Test our simple function
    start_time = time.time()
    encoded_simple = get_dummies(large_brands, 'brand')
    simple_time = time.time() - start_time
    print(f"Our simple function: {simple_time:.4f} seconds")
    
    # Test pandas get_dummies
    df_large = pd.DataFrame({'brand': large_brands})
    start_time = time.time()
    df_encoded_large = pd.get_dummies(df_large, columns=['brand'])
    pandas_time = time.time() - start_time
    print(f"Pandas get_dummies: {pandas_time:.4f} seconds")
    
    # Calculate speedup
    speedup = simple_time / pandas_time
    print(f"\n🚀 Pandas is {speedup:.1f}x faster!")
