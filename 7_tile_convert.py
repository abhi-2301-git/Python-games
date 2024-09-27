def calculate(tile_area, room_area, tile_type):
    tile_req = room_area/tile_area
    if tile_type == "ceramic":
        min_price = tile_req * 2
        max_price = tile_req * 5
    elif tile_type == "porcelain":
        min_price = tile_req * 3
        max_price = tile_req * 10
    elif tile_type == "vinyl":
        min_price = tile_req * 2
        max_price = tile_req * 8
    elif tile_type == "linoleum":
        min_price = tile_req * 2
        max_price = tile_req * 5
    elif tile_type == "granite":
        min_price = tile_req * 5
        max_price = tile_req * 30
    elif tile_type == "travertine":
        min_price = tile_req * 3
        max_price = tile_req * 30
    elif tile_type == "glass mosaics":
        min_price = tile_req * 10
        max_price = tile_req * 50
    elif tile_type == "terazzo":
        min_price = tile_req * 10
        max_price = tile_req * 50
    else:
        print("Invalid choice")
        return None,None

    return min_price , max_price

def main():
    try:
        tile_area = 1 #sq foot
        room_area = int(input("Enter sq foot of room:"))

        #tile selection
        tile_type = input("Ceramic \nPorcelain \nVinyl \nLinoleum \nGranite \nTravertine \nGlass Mosaics \nTerazzo \nChoose one:").lower()
        print(tile_type)
        
        #function call
        min_price,max_price = calculate (tile_area, room_area, tile_type)
        #checking if inavlid choice
        if min_price is not None and max_price is not None:
            print(f"The cost of laying {tile_type.capitalize()} in a {room_area} sq foot area is around ${min_price:.2f} to ${max_price:.2f}.")
        else:
            print("Please enter a valid tile type.")
    except ValueError:
        print("Enter area of room!!")


if __name__ == "__main__":
    main()