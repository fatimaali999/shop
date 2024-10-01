from app import create_app, db
from sqlalchemy import text

app = create_app()

insert_statement = text("""
INSERT INTO product (name, description, price, image_url, category)
VALUES 
    ('Black Women Bag', 'Stylish black bag for everyday use', 59.99, 'http://127.0.0.1:5000/static/images/black-women-bag-2.png', 'Handbags'),
    ('Blue Women Shoe', 'Comfortable blue shoes for casual outings', 49.99, 'http://127.0.0.1:5000/static/images/blue-women-shoe-2.png', 'Shoes'),
    ('Blue Women Shoes', 'Trendy blue shoes for casual outings', 69.99, 'http://127.0.0.1:5000/static/images/blue-women-shoes.png', 'Shoes'),
    ('Canvas Heavy Weight Women Bag', 'Spacious canvas bag for everyday use', 39.99, 'http://127.0.0.1:5000/static/images/canvas-heavy-weight-women-bag.png', 'Handbags'),
    ('Cartier Brown Women Bag', 'Elegant brown bag from Cartier', 199.99, 'http://127.0.0.1:5000/static/images/cartier-brown-women-bag.png', 'Handbags'),
    ('Cartier Red Women Bag', 'Stylish red bag from Cartier', 199.99, 'http://127.0.0.1:5000/static/images/cartier-red-women-bag.png', 'Handbags'),
    ('Christmas Tree with Gifts', 'Decorative Christmas tree with gifts', 79.99, 'http://127.0.0.1:5000/static/images/christmas-tree-with-gifts.png', 'Decorations'),
    ('Comb', 'Essential comb for hair styling', 5.99, 'http://127.0.0.1:5000/static/images/comb.png', 'Accessories'),
    ('Diamond Earring', 'Stunning diamond earrings for any occasion', 199.99, 'http://127.0.0.1:5000/static/images/diamond-earring-2.png', 'Jewelry'),
    ('Diamond Pendant', 'Elegant diamond pendant for special occasions', 149.99, 'http://127.0.0.1:5000/static/images/diamond-pendant-3.png', 'Jewelry'),
    ('Fur Coat Women Clothing', 'Luxurious fur coat for winter', 299.99, 'http://127.0.0.1:5000/static/images/fur-coat-women-clothing-shearling-coats.png', 'Clothing'),
    ('Girl Dress', 'Stylish dress for girls', 49.99, 'http://127.0.0.1:5000/static/images/girl-dress-2.png', 'Womens Clothes'),
    ('Gold Diamond Necklace', 'Beautiful gold diamond necklace', 249.99, 'http://127.0.0.1:5000/static/images/gold-diamond-necklace.png', 'Jewelry'),
    ('Gold Ring', 'Elegant gold ring', 149.99, 'http://127.0.0.1:5000/static/images/gold-ring-5.png', 'Jewelry'),
    ('Hanging Light', 'Stylish hanging light fixture', 89.99, 'http://127.0.0.1:5000/static/images/hanging-light.png', 'Lighting'),
    ('High Heels Shoes', 'Fashionable high heels for special occasions', 89.99, 'http://127.0.0.1:5000/static/images/high-heels-shoes.png', 'Shoes'),
    ('Lipstick', 'Luxurious lipstick in various shades', 29.99, 'http://127.0.0.1:5000/static/images/lipstick-2.png', 'Cosmetics'),
    ('Louis Vuitton Women Bag', 'Stylish Louis Vuitton bag', 399.99, 'http://127.0.0.1:5000/static/images/louis-vuitton-women-bag-2.png', 'Handbags'),
    ('Love Heart Frame', 'Decorative heart frame for photos', 24.99, 'http://127.0.0.1:5000/static/images/love-heart-frame.png', 'Decorations'),
    ('Mirror', 'Stylish mirror for home decoration', 59.99, 'http://127.0.0.1:5000/static/images/mirror-30.png', 'Decorations'),
    ('Nail Polish Bottle', 'Colorful nail polish for manicures', 9.99, 'http://127.0.0.1:5000/static/images/nail-polish-bottle-4.png', 'Cosmetics'),
    ('Paint Brush', 'Quality paint brush for artists', 14.99, 'http://127.0.0.1:5000/static/images/paint-brush-23.png', 'Art Supplies'),
    ('Rachel Zoe Tonal Cream Jacket', 'Stylish cream jacket for women', 129.99, 'http://127.0.0.1:5000/static/images/rachel-zoe-tonal-cream-cheetah-faux-macgraw-jacket.png', 'Clothing'),
    ('Roller Skates', 'Fun roller skates for kids and adults', 79.99, 'http://127.0.0.1:5000/static/images/roller-skates-29.png', 'Sports'),
    ('Running Shoes', 'Comfortable running shoes', 69.99, 'http://127.0.0.1:5000/static/images/running-shoes-9.png', 'Shoes'),
    ('Silver Ring with Diamond', 'Elegant silver ring with diamond', 199.99, 'http://127.0.0.1:5000/static/images/silver-ring-with-diamond-8.png', 'Jewelry'),
    ('Super Duster Brush', 'Versatile duster brush for cleaning', 15.99, 'http://127.0.0.1:5000/static/images/super-duster-brush.png', 'Cleaning Supplies'),
    ('Two Teddy Bears Gift', 'Adorable teddy bears for gifts', 29.99, 'http://127.0.0.1:5000/static/images/two-teddy-bears-gift.png', 'Toys'),
    ('Women Dress', 'Elegant dress for women', 89.99, 'http://127.0.0.1:5000/static/images/women-dress-2.png', 'Womens Clothes'),
    ('Women Dress 5', 'Stylish dress for women', 89.99, 'http://127.0.0.1:5000/static/images/women-dress-5.png', 'Womens Clothes');
""")

# Set up application context
with app.app_context():
    with db.session.begin():
        db.session.execute(insert_statement)
        db.session.commit()

print("Products inserted successfully!")

