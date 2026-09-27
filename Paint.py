class House:
    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return 2.5 * self.wall_area


class Paint:
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19


class DiscountedPaint(Paint):
    def discounted_price(self, discount_percentage):
        original_price = self.total_price()
        discount_amount = original_price * discount_percentage / 100
        return original_price - discount_amount


# Example usage
house = House(100)

buckets = house.paint_needed()
print("Paint needed:", buckets, "buckets")

paint = Paint(buckets, "white")
print("Total price:", paint.total_price())

discounted_paint = DiscountedPaint(buckets, "white")
print("Discounted price:", discounted_paint.discounted_price(10))