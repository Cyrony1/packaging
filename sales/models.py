from django.db import models


class Customer(models.Model):

    CORRIER_CHOICES = [
        ('Fedex','Fedex'),
        ('UPS', 'UPS'),
        ('DHL', 'DHL'),
    ]


    title = models.CharField(max_length= 255)
    name = models.CharField(max_length=255)
    address = models.TextField()
    web = models.CharField(max_length=255)
    country = models.CharField(max_length=10)
    corrier = models.CharField(max_length=5, choices=CORRIER_CHOICES, default='Fedex')
    account = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping_address = models.TextField()


class Product(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sku = models.CharField(max_length=50)
    customer_product_number = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=7, decimal_places=4)
    case_pack = models.IntegerField()
    meas_L = models.IntegerField()
    meas_W = models.IntegerField()
    meas_H = models.IntegerField()
    nw = models.DecimalField(max_digits=4, decimal_places=1)
    gw = models.DecimalField(max_digits=4, decimal_places=1)

    

class Order(models.Model):
    FOB = 'FOB' 
    CIF = 'CIF'
    SHIPPING_TERM_CHOICES = [
        (FOB, 'FOB'),
        (CIF, 'CIF'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    customer_po = models.CharField(max_length=255)
    pi = models.CharField(max_length=255, null=True)
    order_date = models.DateField(auto_now_add=True)
    shipping_term = models.CharField(max_length=3, choices=SHIPPING_TERM_CHOICES, default=FOB)
    port = models.CharField(max_length=255)
    expect_shipping_date = models.DateField(auto_now_add=False, null=False)
    exact_shipping_date = models.DateField(auto_now_add=False, null= True)
    ship_to = models.TextField()
    shipping_method = models.CharField(max_length=255)
    payment_term = models.CharField(max_length=255)
    commission_apply = models.CharField(max_length=255, null = True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    description = models.TextField() 
    quantity = models.IntegerField() 
    unit_price = models.DecimalField(max_digits=7, decimal_places=4)
    commission_price = models.DecimalField(max_digits=7, decimal_places=5)
    

class Invoice(models.Model):

    INVOICE_CHOICES = (
        ('PAID', 'PAID'),
        ('OPEN','OPEN'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    invoice_date = models.DateField(auto_created=True)
    shipto = models.TextField()
    due_date = models.DateField(auto_created=False)
    statue = models.CharField(max_length=4, choices=INVOICE_CHOICES, default='OPEN')


class InvoiceItem(models.Model):
    Invoice =models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=4)



class Lead(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date = models.DateField(auto_created=True)
    subject = models.CharField(max_length=255)
    detail = models.TextField()
    status = models.CharField(max_length=3)


class Sample(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    subject = models.CharField(max_length=255)
    send_date = models.DateField(auto_created=True)
    follow_up_date = models.DateField(auto_created=True)
    tracking = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.subject