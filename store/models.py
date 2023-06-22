from django.db import models
from mptt.models import TreeForeignKey, MPTTModel
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def image_upload_path(instance, filename):
    # Construct the upload path with the product ID
    return f'products_img/{instance.product.id}/{filename}'


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_(
        "Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE,
                            null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):

    name = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_products")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="category_products")
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )

    description = models.TextField(blank=True)
    type = models.ForeignKey(
        ProductType, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    old_price = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.name


class Detail(models.Model):

    value = models.CharField(max_length=255, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_details")

    def __str__(self):
        return f'{self.product.name}, {self.value}'


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product
    specifiction or features for the product types.
    """

    name = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Required"),
        max_length=255
    )
    product_type = models.ManyToManyField(
        ProductType, related_name="specifications")

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    specification = models.ForeignKey(
        ProductSpecification, on_delete=models.CASCADE)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Product specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    variant = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_image")
    url = models.ImageField(
        verbose_name=_("url"),
        help_text=_("Upload a product image"),
        upload_to=image_upload_path
    )
    alt_text = models.CharField(
        verbose_name=_("Alternative text"),
        help_text=_("Please add alternative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return self.product.name
