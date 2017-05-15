# Grocery Digital Coupon Automation


## Usage
The script only supports [Shoprite](http://www.shoprite.com) and [Stop and Shop](http://www.stopandshop.com/) for now:

1. `python grocery_coupons.py shoprite`
2. `python grocery_coupons.py shop_and_shop`


## Dependencies
[Selenium](http://selenium-python.readthedocs.io/index.html)


## More Info

### What are grocery digital coupons?
My local grocery stores - [ShopRite](http://www.shoprite.com) and [Stop and Shop](http://www.stopandshop.com/) - have a "digital coupon" feature, by which you can log onto their website and add "digital" coupons to your store loyalty card. If you buy a product and the corresponding digital coupon is added to your loyalty card, you'll save some money upon checkout.

### So what's the problem?
The problem is that the digital coupons have to be added manually. If you buy something and the coupon isn't present on your loyalty card at the time of checkout, you won't get the discount.

### Wow, that's dumb.
Yep.

### What's the solution?
The script adds *all* digital coupons to your card each week. Then, you'll automatically get the discount when you buy a product without having to do any legwork.

### So how does the script work?
The script uses [Selenium](http://selenium-python.readthedocs.io/index.html) to launch the grocery store's website, login with your loyalty card information, and automatically add each available coupon to your card.

### Where is my login information saved?
The file `config_example.ini` contains an example of how to set up the config file. This file will need to be renamed `config.ini` in order for the script to work.

### How do I launch the script?
Launch it with an argument for the store you want to access. Right now the two options are:

1. `python grocery_coupons.py shoprite`
2. `python grocery_coupons.py shop_and_shop`


## What's next?

The script only supports ShopRite and Stop and Shop for now, so the addition of other grocery stories would be great. It appears that [Giant's website](https://giantfoodstores.com/) looks similar to Stop and Shop since they're [owned by the same company](https://en.wikipedia.org/wiki/Stop_%26_Shop/Giant-Landover), so I assume this would be easy to integrate.

## Contact
You can contact the author, Sheil Naik, [on Twitter](http://www.twitter.com/sheilnaik).
