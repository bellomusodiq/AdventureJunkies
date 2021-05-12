# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = types_to_generate_from_dict(json.loads(json_string))

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union, cast

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


@dataclass
class AmazonBestSellers:
    category: Optional[str] = None
    sub_category: Optional[str] = None
    sub_category_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "AmazonBestSellers":
        assert isinstance(obj, dict)
        category = from_union([from_str, from_none], obj.get("Category"))
        sub_category = from_union([from_str, from_none], obj.get("SubCategory"))
        sub_category_id = from_union([from_str, from_none], obj.get("SubCategoryID"))
        return AmazonBestSellers(category, sub_category, sub_category_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Category"] = from_union([from_str, from_none], self.category)
        result["SubCategory"] = from_union([from_str, from_none], self.sub_category)
        result["SubCategoryID"] = from_union(
            [from_str, from_none], self.sub_category_id
        )
        return result


@dataclass
class BestBuyBestSellers:
    category: Optional[str] = None
    sub_category: Optional[str] = None
    sub_category_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "BestBuyBestSellers":
        assert isinstance(obj, dict)
        category = from_union([from_str, from_none], obj.get("Category"))
        sub_category = from_union([from_str, from_none], obj.get("SubCategory"))
        sub_category_id = from_union([from_str, from_none], obj.get("SubCategoryID"))
        return BestBuyBestSellers(category, sub_category, sub_category_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Category"] = from_union([from_str, from_none], self.category)
        result["SubCategory"] = from_union([from_str, from_none], self.sub_category)
        result["SubCategoryID"] = from_union(
            [from_str, from_none], self.sub_category_id
        )
        return result


@dataclass
class BestSellers:
    amazon: Optional[AmazonBestSellers] = None
    best_buy: Optional[BestBuyBestSellers] = None

    @staticmethod
    def from_dict(obj: Any) -> "BestSellers":
        assert isinstance(obj, dict)
        amazon = from_union([AmazonBestSellers.from_dict, from_none], obj.get("Amazon"))
        best_buy = from_union(
            [BestBuyBestSellers.from_dict, from_none], obj.get("BestBuy")
        )
        return BestSellers(amazon, best_buy)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Amazon"] = from_union(
            [lambda x: to_class(AmazonBestSellers, x), from_none], self.amazon
        )
        result["BestBuy"] = from_union(
            [lambda x: to_class(BestBuyBestSellers, x), from_none], self.best_buy
        )
        return result


@dataclass
class ProductBrand:
    description: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "ProductBrand":
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("Description"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return ProductBrand(description, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Description"] = from_union([from_str, from_none], self.description)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class ProductDecisionFeature:
    body: Optional[str] = None
    image_url: Optional[str] = None
    summary: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "ProductDecisionFeature":
        assert isinstance(obj, dict)
        body = from_union([from_str, from_none], obj.get("Body"))
        image_url = from_union([from_str, from_none], obj.get("ImageURL"))
        summary = from_union([from_str, from_none], obj.get("Summary"))
        return ProductDecisionFeature(body, image_url, summary)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Body"] = from_union([from_str, from_none], self.body)
        result["ImageURL"] = from_union([from_str, from_none], self.image_url)
        result["Summary"] = from_union([from_str, from_none], self.summary)
        return result


@dataclass
class CategoryProductType:
    description: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "CategoryProductType":
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("Description"))
        image_url = from_union([from_str, from_none], obj.get("ImageURL"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return CategoryProductType(description, image_url, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Description"] = from_union([from_str, from_none], self.description)
        result["ImageURL"] = from_union([from_str, from_none], self.image_url)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class CategoryOverview:
    brands: Optional[List[ProductBrand]] = None
    category_description: Optional[str] = None
    category_name: Optional[str] = None
    decision_features: Optional[List[ProductDecisionFeature]] = None
    header_image_url: Optional[str] = None
    product_types: Optional[List[CategoryProductType]] = None

    @staticmethod
    def from_dict(obj: Any) -> "CategoryOverview":
        assert isinstance(obj, dict)
        brands = from_union(
            [lambda x: from_list(ProductBrand.from_dict, x), from_none],
            obj.get("Brands"),
        )
        category_description = from_union(
            [from_str, from_none], obj.get("CategoryDescription")
        )
        category_name = from_union([from_str, from_none], obj.get("CategoryName"))
        decision_features = from_union(
            [lambda x: from_list(ProductDecisionFeature.from_dict, x), from_none],
            obj.get("DecisionFeatures"),
        )
        header_image_url = from_union([from_str, from_none], obj.get("HeaderImageURL"))
        product_types = from_union(
            [lambda x: from_list(CategoryProductType.from_dict, x), from_none],
            obj.get("ProductTypes"),
        )
        return CategoryOverview(
            brands,
            category_description,
            category_name,
            decision_features,
            header_image_url,
            product_types,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["Brands"] = from_union(
            [lambda x: from_list(lambda x: to_class(ProductBrand, x), x), from_none],
            self.brands,
        )
        result["CategoryDescription"] = from_union(
            [from_str, from_none], self.category_description
        )
        result["CategoryName"] = from_union([from_str, from_none], self.category_name)
        result["DecisionFeatures"] = from_union(
            [
                lambda x: from_list(lambda x: to_class(ProductDecisionFeature, x), x),
                from_none,
            ],
            self.decision_features,
        )
        result["HeaderImageURL"] = from_union(
            [from_str, from_none], self.header_image_url
        )
        result["ProductTypes"] = from_union(
            [
                lambda x: from_list(lambda x: to_class(CategoryProductType, x), x),
                from_none,
            ],
            self.product_types,
        )
        return result


@dataclass
class UserProfile:
    image_url: Optional[str] = None
    name: Optional[str] = None
    profile_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "UserProfile":
        assert isinstance(obj, dict)
        image_url = from_union([from_str, from_none], obj.get("ImageURL"))
        name = from_union([from_str, from_none], obj.get("Name"))
        profile_url = from_union([from_str, from_none], obj.get("ProfileURL"))
        return UserProfile(image_url, name, profile_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ImageURL"] = from_union([from_str, from_none], self.image_url)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["ProfileURL"] = from_union([from_str, from_none], self.profile_url)
        return result


@dataclass
class ProductImage:
    caption: Optional[str] = None
    image_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "ProductImage":
        assert isinstance(obj, dict)
        caption = from_union([from_str, from_none], obj.get("Caption"))
        image_url = from_union([from_str, from_none], obj.get("ImageURL"))
        return ProductImage(caption, image_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Caption"] = from_union([from_str, from_none], self.caption)
        result["ImageURL"] = from_union([from_str, from_none], self.image_url)
        return result


@dataclass
class ReviewFacet:
    body: Optional[str] = None
    summary: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "ReviewFacet":
        assert isinstance(obj, dict)
        body = from_union([from_str, from_none], obj.get("Body"))
        summary = from_union([from_str, from_none], obj.get("Summary"))
        return ReviewFacet(body, summary)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Body"] = from_union([from_str, from_none], self.body)
        result["Summary"] = from_union([from_str, from_none], self.summary)
        return result


@dataclass
class RatingBreakdown:
    cons: Optional[List[ReviewFacet]] = None
    pros: Optional[List[ReviewFacet]] = None

    @staticmethod
    def from_dict(obj: Any) -> "RatingBreakdown":
        assert isinstance(obj, dict)
        cons = from_union(
            [lambda x: from_list(ReviewFacet.from_dict, x), from_none], obj.get("Cons")
        )
        pros = from_union(
            [lambda x: from_list(ReviewFacet.from_dict, x), from_none], obj.get("Pros")
        )
        return RatingBreakdown(cons, pros)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Cons"] = from_union(
            [lambda x: from_list(lambda x: to_class(ReviewFacet, x), x), from_none],
            self.cons,
        )
        result["Pros"] = from_union(
            [lambda x: from_list(lambda x: to_class(ReviewFacet, x), x), from_none],
            self.pros,
        )
        return result


@dataclass
class Rating:
    best_rating: Optional[str] = None
    best_sub_rating: Optional[int] = None
    rating_value: Optional[str] = None
    sub_ratings: Optional[Dict[str, str]] = None
    worst_rating: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Rating":
        assert isinstance(obj, dict)
        best_rating = from_union([from_str, from_none], obj.get("BestRating"))
        best_sub_rating = from_union([from_int, from_none], obj.get("BestSubRating"))
        rating_value = from_union([from_str, from_none], obj.get("RatingValue"))
        sub_ratings = from_union(
            [lambda x: from_dict(from_str, x), from_none], obj.get("SubRatings")
        )
        worst_rating = from_union([from_str, from_none], obj.get("WorstRating"))
        return Rating(
            best_rating, best_sub_rating, rating_value, sub_ratings, worst_rating
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["BestRating"] = from_union([from_str, from_none], self.best_rating)
        result["BestSubRating"] = from_union(
            [from_int, from_none], self.best_sub_rating
        )
        result["RatingValue"] = from_union([from_str, from_none], self.rating_value)
        result["SubRatings"] = from_union(
            [lambda x: from_dict(from_str, x), from_none], self.sub_ratings
        )
        result["WorstRating"] = from_union([from_str, from_none], self.worst_rating)
        return result


@dataclass
class ReviewSnippet:
    begin: Optional[int] = None
    end: Optional[int] = None
    polarity: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "ReviewSnippet":
        assert isinstance(obj, dict)
        begin = from_union([from_int, from_none], obj.get("Begin"))
        end = from_union([from_int, from_none], obj.get("End"))
        polarity = from_union([from_int, from_none], obj.get("Polarity"))
        return ReviewSnippet(begin, end, polarity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Begin"] = from_union([from_int, from_none], self.begin)
        result["End"] = from_union([from_int, from_none], self.end)
        result["Polarity"] = from_union([from_int, from_none], self.polarity)
        return result


@dataclass
class AggregateRatingHistogram:
    rating_value: Optional[int] = None
    review_count: Optional[int] = None
    review_percent: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "AggregateRatingHistogram":
        assert isinstance(obj, dict)
        rating_value = from_union([from_int, from_none], obj.get("RatingValue"))
        review_count = from_union([from_int, from_none], obj.get("ReviewCount"))
        review_percent = from_union([from_int, from_none], obj.get("ReviewPercent"))
        return AggregateRatingHistogram(rating_value, review_count, review_percent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["RatingValue"] = from_union([from_int, from_none], self.rating_value)
        result["ReviewCount"] = from_union([from_int, from_none], self.review_count)
        result["ReviewPercent"] = from_union([from_int, from_none], self.review_percent)
        return result


@dataclass
class AggregateRating:
    awards: Optional[str] = None
    best_rating: Optional[str] = None
    rating_count: Optional[str] = None
    rating_histogram: Optional[List[AggregateRatingHistogram]] = None
    rating_value: Optional[str] = None
    review_count: Optional[str] = None
    sub_ratings: Optional[Dict[str, str]] = None
    worst_rating: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "AggregateRating":
        assert isinstance(obj, dict)
        awards = from_union([from_str, from_none], obj.get("Awards"))
        best_rating = from_union([from_str, from_none], obj.get("BestRating"))
        rating_count = from_union([from_str, from_none], obj.get("RatingCount"))
        rating_histogram = from_union(
            [lambda x: from_list(AggregateRatingHistogram.from_dict, x), from_none],
            obj.get("RatingHistogram"),
        )
        rating_value = from_union([from_str, from_none], obj.get("RatingValue"))
        review_count = from_union([from_str, from_none], obj.get("ReviewCount"))
        sub_ratings = from_union(
            [lambda x: from_dict(from_str, x), from_none], obj.get("SubRatings")
        )
        worst_rating = from_union([from_str, from_none], obj.get("WorstRating"))
        return AggregateRating(
            awards,
            best_rating,
            rating_count,
            rating_histogram,
            rating_value,
            review_count,
            sub_ratings,
            worst_rating,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["Awards"] = from_union([from_str, from_none], self.awards)
        result["BestRating"] = from_union([from_str, from_none], self.best_rating)
        result["RatingCount"] = from_union([from_str, from_none], self.rating_count)
        result["RatingHistogram"] = from_union(
            [
                lambda x: from_list(lambda x: to_class(AggregateRatingHistogram, x), x),
                from_none,
            ],
            self.rating_histogram,
        )
        result["RatingValue"] = from_union([from_str, from_none], self.rating_value)
        result["ReviewCount"] = from_union([from_str, from_none], self.review_count)
        result["SubRatings"] = from_union(
            [lambda x: from_dict(from_str, x), from_none], self.sub_ratings
        )
        result["WorstRating"] = from_union([from_str, from_none], self.worst_rating)
        return result


@dataclass
class ProductAttributeValue:
    image_url: Optional[str] = None
    is_available: Optional[bool] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "ProductAttributeValue":
        assert isinstance(obj, dict)
        image_url = from_union([from_str, from_none], obj.get("ImageURL"))
        is_available = from_union([from_bool, from_none], obj.get("IsAvailable"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return ProductAttributeValue(image_url, is_available, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ImageURL"] = from_union([from_str, from_none], self.image_url)
        result["IsAvailable"] = from_union([from_bool, from_none], self.is_available)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class ProductAttribute:
    name: Optional[str] = None
    type: Optional[str] = None
    values: Optional[List[ProductAttributeValue]] = None

    @staticmethod
    def from_dict(obj: Any) -> "ProductAttribute":
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        type = from_union([from_str, from_none], obj.get("Type"))
        values = from_union(
            [lambda x: from_list(ProductAttributeValue.from_dict, x), from_none],
            obj.get("Values"),
        )
        return ProductAttribute(name, type, values)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Type"] = from_union([from_str, from_none], self.type)
        result["Values"] = from_union(
            [
                lambda x: from_list(lambda x: to_class(ProductAttributeValue, x), x),
                from_none,
            ],
            self.values,
        )
        return result


@dataclass
class Offer:
    availability: Optional[str] = None
    available_delivery_method: Optional[str] = None
    has_free_shipping: Optional[bool] = None
    high_price: Optional[float] = None
    inventory_level: Optional[int] = None
    is_best_seller: Optional[bool] = None
    item_condition: Optional[str] = None
    name: Optional[str] = None
    original_price: Optional[str] = None
    price: Optional[str] = None
    price_currency: Optional[str] = None
    price_usd: Optional[str] = None
    seller: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Offer":
        assert isinstance(obj, dict)
        availability = from_union([from_str, from_none], obj.get("Availability"))
        available_delivery_method = from_union(
            [from_str, from_none], obj.get("AvailableDeliveryMethod")
        )
        has_free_shipping = from_union(
            [from_bool, from_none], obj.get("HasFreeShipping")
        )
        high_price = from_union([from_float, from_none], obj.get("HighPrice"))
        inventory_level = from_union([from_int, from_none], obj.get("InventoryLevel"))
        is_best_seller = from_union([from_bool, from_none], obj.get("IsBestSeller"))
        item_condition = from_union([from_str, from_none], obj.get("ItemCondition"))
        name = from_union([from_str, from_none], obj.get("Name"))
        original_price = from_union([from_str, from_none], obj.get("OriginalPrice"))
        price = from_union([from_str, from_none], obj.get("Price"))
        price_currency = from_union([from_str, from_none], obj.get("PriceCurrency"))
        price_usd = from_union([from_str, from_none], obj.get("PriceUSD"))
        seller = from_union([from_str, from_none], obj.get("Seller"))
        url = from_union([from_str, from_none], obj.get("URL"))
        return Offer(
            availability,
            available_delivery_method,
            has_free_shipping,
            high_price,
            inventory_level,
            is_best_seller,
            item_condition,
            name,
            original_price,
            price,
            price_currency,
            price_usd,
            seller,
            url,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["Availability"] = from_union([from_str, from_none], self.availability)
        result["AvailableDeliveryMethod"] = from_union(
            [from_str, from_none], self.available_delivery_method
        )
        result["HasFreeShipping"] = from_union(
            [from_bool, from_none], self.has_free_shipping
        )
        result["HighPrice"] = from_union([to_float, from_none], self.high_price)
        result["InventoryLevel"] = from_union(
            [from_int, from_none], self.inventory_level
        )
        result["IsBestSeller"] = from_union([from_bool, from_none], self.is_best_seller)
        result["ItemCondition"] = from_union([from_str, from_none], self.item_condition)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["OriginalPrice"] = from_union([from_str, from_none], self.original_price)
        result["Price"] = from_union([from_str, from_none], self.price)
        result["PriceCurrency"] = from_union([from_str, from_none], self.price_currency)
        result["PriceUSD"] = from_union([from_str, from_none], self.price_usd)
        result["Seller"] = from_union([from_str, from_none], self.seller)
        result["URL"] = from_union([from_str, from_none], self.url)
        return result


class ProductType(Enum):
    BEST_SELLERS = "BestSellers"
    BUYING_GUIDES = "BuyingGuides"
    COMPARISON = "Comparison"
    EXPERT_REVIEWS = "ExpertReviews"
    PRODUCT = "Product"
    REVIEW_ONLY = "ReviewOnly"
    SEARCH_RESULTS = "SearchResults"
    SIMILAR = "Similar"
    UNKNOWN = "Unknown"


@dataclass
class Review:
    author: Optional[str] = None
    author_profile: Optional[UserProfile] = None
    date_modified: Optional[str] = None
    date_published: Optional[str] = None
    description: Optional[str] = None
    images: Optional[List[ProductImage]] = None
    item_reviewed: Optional["Product"] = None
    name: Optional[str] = None
    num_people_found_helpful: Optional[int] = None
    publisher: Optional[str] = None
    rating_breakdown: Optional[RatingBreakdown] = None
    review_body: Optional[str] = None
    review_rating: Optional[Rating] = None
    snippets: Optional[List[ReviewSnippet]] = None
    summary: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Review":
        assert isinstance(obj, dict)
        author = from_union([from_str, from_none], obj.get("Author"))
        author_profile = from_union(
            [UserProfile.from_dict, from_none], obj.get("AuthorProfile")
        )
        date_modified = from_union([from_str, from_none], obj.get("DateModified"))
        date_published = from_union([from_str, from_none], obj.get("DatePublished"))
        description = from_union([from_str, from_none], obj.get("Description"))
        images = from_union(
            [lambda x: from_list(ProductImage.from_dict, x), from_none],
            obj.get("Images"),
        )
        item_reviewed = from_union(
            [Product.from_dict, from_none], obj.get("ItemReviewed")
        )
        name = from_union([from_str, from_none], obj.get("Name"))
        num_people_found_helpful = from_union(
            [from_int, from_none], obj.get("NumPeopleFoundHelpful")
        )
        publisher = from_union([from_str, from_none], obj.get("Publisher"))
        rating_breakdown = from_union(
            [RatingBreakdown.from_dict, from_none], obj.get("RatingBreakdown")
        )
        review_body = from_union([from_str, from_none], obj.get("ReviewBody"))
        review_rating = from_union(
            [Rating.from_dict, from_none], obj.get("ReviewRating")
        )
        snippets = from_union(
            [lambda x: from_list(ReviewSnippet.from_dict, x), from_none],
            obj.get("Snippets"),
        )
        summary = from_union([from_str, from_none], obj.get("Summary"))
        return Review(
            author,
            author_profile,
            date_modified,
            date_published,
            description,
            images,
            item_reviewed,
            name,
            num_people_found_helpful,
            publisher,
            rating_breakdown,
            review_body,
            review_rating,
            snippets,
            summary,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["Author"] = from_union([from_str, from_none], self.author)
        result["AuthorProfile"] = from_union(
            [lambda x: to_class(UserProfile, x), from_none], self.author_profile
        )
        result["DateModified"] = from_union([from_str, from_none], self.date_modified)
        result["DatePublished"] = from_union([from_str, from_none], self.date_published)
        result["Description"] = from_union([from_str, from_none], self.description)
        result["Images"] = from_union(
            [lambda x: from_list(lambda x: to_class(ProductImage, x), x), from_none],
            self.images,
        )
        result["ItemReviewed"] = from_union(
            [lambda x: to_class(Product, x), from_none], self.item_reviewed
        )
        result["Name"] = from_union([from_str, from_none], self.name)
        result["NumPeopleFoundHelpful"] = from_union(
            [from_int, from_none], self.num_people_found_helpful
        )
        result["Publisher"] = from_union([from_str, from_none], self.publisher)
        result["RatingBreakdown"] = from_union(
            [lambda x: to_class(RatingBreakdown, x), from_none], self.rating_breakdown
        )
        result["ReviewBody"] = from_union([from_str, from_none], self.review_body)
        result["ReviewRating"] = from_union(
            [lambda x: to_class(Rating, x), from_none], self.review_rating
        )
        result["Snippets"] = from_union(
            [lambda x: from_list(lambda x: to_class(ReviewSnippet, x), x), from_none],
            self.snippets,
        )
        result["Summary"] = from_union([from_str, from_none], self.summary)
        return result


@dataclass
class Product:
    aggregate_rating: Optional[AggregateRating] = None
    attributes: Optional[List[ProductAttribute]] = None
    brand: Optional[str] = None
    callout: Optional[str] = None
    description: Optional[str] = None
    description_list: Optional[List[str]] = None
    gtin13: Optional[str] = None
    images: Optional[List[ProductImage]] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
    offers: Optional[List[Offer]] = None
    product_type: Optional[ProductType] = None
    rank: Optional[int] = None
    related_products: Optional[List["Product"]] = None
    reviews: Optional[List[Review]] = None
    review_url: Optional[str] = None
    url: Optional[str] = None
    wirecutter_chapter: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Product":
        assert isinstance(obj, dict)
        aggregate_rating = from_union(
            [AggregateRating.from_dict, from_none], obj.get("AggregateRating")
        )
        attributes = from_union(
            [lambda x: from_list(ProductAttribute.from_dict, x), from_none],
            obj.get("Attributes"),
        )
        brand = from_union([from_str, from_none], obj.get("Brand"))
        callout = from_union([from_str, from_none], obj.get("Callout"))
        description = from_union([from_str, from_none], obj.get("Description"))
        description_list = from_union(
            [lambda x: from_list(from_str, x), from_none], obj.get("DescriptionList")
        )
        gtin13 = from_union([from_str, from_none], obj.get("Gtin13"))
        images = from_union(
            [lambda x: from_list(ProductImage.from_dict, x), from_none],
            obj.get("Images"),
        )
        image_url = from_union([from_str, from_none], obj.get("ImageURL"))
        name = from_union([from_str, from_none], obj.get("Name"))
        offers = from_union(
            [lambda x: from_list(Offer.from_dict, x), from_none], obj.get("Offers")
        )
        product_type = from_union([ProductType, from_none], obj.get("ProductType"))
        rank = from_union([from_int, from_none], obj.get("Rank"))
        related_products = from_union(
            [lambda x: from_list(Product.from_dict, x), from_none],
            obj.get("RelatedProducts"),
        )
        reviews = from_union(
            [lambda x: from_list(Review.from_dict, x), from_none], obj.get("Reviews")
        )
        review_url = from_union([from_str, from_none], obj.get("ReviewURL"))
        url = from_union([from_str, from_none], obj.get("URL"))
        wirecutter_chapter = from_union(
            [from_str, from_none], obj.get("WirecutterChapter")
        )
        return Product(
            aggregate_rating,
            attributes,
            brand,
            callout,
            description,
            description_list,
            gtin13,
            images,
            image_url,
            name,
            offers,
            product_type,
            rank,
            related_products,
            reviews,
            review_url,
            url,
            wirecutter_chapter,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["AggregateRating"] = from_union(
            [lambda x: to_class(AggregateRating, x), from_none], self.aggregate_rating
        )
        result["Attributes"] = from_union(
            [
                lambda x: from_list(lambda x: to_class(ProductAttribute, x), x),
                from_none,
            ],
            self.attributes,
        )
        result["Brand"] = from_union([from_str, from_none], self.brand)
        result["Callout"] = from_union([from_str, from_none], self.callout)
        result["Description"] = from_union([from_str, from_none], self.description)
        result["DescriptionList"] = from_union(
            [lambda x: from_list(from_str, x), from_none], self.description_list
        )
        result["Gtin13"] = from_union([from_str, from_none], self.gtin13)
        result["Images"] = from_union(
            [lambda x: from_list(lambda x: to_class(ProductImage, x), x), from_none],
            self.images,
        )
        result["ImageURL"] = from_union([from_str, from_none], self.image_url)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Offers"] = from_union(
            [lambda x: from_list(lambda x: to_class(Offer, x), x), from_none],
            self.offers,
        )
        result["ProductType"] = from_union(
            [lambda x: to_enum(ProductType, x), from_none], self.product_type
        )
        result["Rank"] = from_union([from_int, from_none], self.rank)
        result["RelatedProducts"] = from_union(
            [lambda x: from_list(lambda x: to_class(Product, x), x), from_none],
            self.related_products,
        )
        result["Reviews"] = from_union(
            [lambda x: from_list(lambda x: to_class(Review, x), x), from_none],
            self.reviews,
        )
        result["ReviewURL"] = from_union([from_str, from_none], self.review_url)
        result["URL"] = from_union([from_str, from_none], self.url)
        result["WirecutterChapter"] = from_union(
            [from_str, from_none], self.wirecutter_chapter
        )
        return result


@dataclass
class Question:
    answer_snippets: Optional[List[str]] = None
    answer_url: Optional[str] = None
    popularity: Optional[int] = None
    question_snippet: Optional[str] = None
    question_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "Question":
        assert isinstance(obj, dict)
        answer_snippets = from_union(
            [lambda x: from_list(from_str, x), from_none], obj.get("AnswerSnippets")
        )
        answer_url = from_union([from_str, from_none], obj.get("AnswerURL"))
        popularity = from_union([from_int, from_none], obj.get("Popularity"))
        question_snippet = from_union([from_str, from_none], obj.get("QuestionSnippet"))
        question_url = from_union([from_str, from_none], obj.get("QuestionURL"))
        return Question(
            answer_snippets, answer_url, popularity, question_snippet, question_url
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["AnswerSnippets"] = from_union(
            [lambda x: from_list(from_str, x), from_none], self.answer_snippets
        )
        result["AnswerURL"] = from_union([from_str, from_none], self.answer_url)
        result["Popularity"] = from_union([from_int, from_none], self.popularity)
        result["QuestionSnippet"] = from_union(
            [from_str, from_none], self.question_snippet
        )
        result["QuestionURL"] = from_union([from_str, from_none], self.question_url)
        return result


@dataclass
class FilterOption:
    image_url: Optional[str] = None
    is_selected: Optional[bool] = None
    name: Optional[str] = None
    rank: Optional[int] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> "FilterOption":
        assert isinstance(obj, dict)
        image_url = from_union([from_str, from_none], obj.get("ImageURL"))
        is_selected = from_union([from_bool, from_none], obj.get("IsSelected"))
        name = from_union([from_str, from_none], obj.get("Name"))
        rank = from_union([from_int, from_none], obj.get("Rank"))
        url = from_union([from_str, from_none], obj.get("URL"))
        return FilterOption(image_url, is_selected, name, rank, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ImageURL"] = from_union([from_str, from_none], self.image_url)
        result["IsSelected"] = from_union([from_bool, from_none], self.is_selected)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Rank"] = from_union([from_int, from_none], self.rank)
        result["URL"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class SearchFilter:
    filter_type: Optional[str] = None
    name: Optional[str] = None
    options: Optional[List[FilterOption]] = None
    position: Optional[int] = None
    rank: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "SearchFilter":
        assert isinstance(obj, dict)
        filter_type = from_union([from_str, from_none], obj.get("FilterType"))
        name = from_union([from_str, from_none], obj.get("Name"))
        options = from_union(
            [lambda x: from_list(FilterOption.from_dict, x), from_none],
            obj.get("Options"),
        )
        position = from_union([from_int, from_none], obj.get("Position"))
        rank = from_union([from_int, from_none], obj.get("Rank"))
        return SearchFilter(filter_type, name, options, position, rank)

    def to_dict(self) -> dict:
        result: dict = {}
        result["FilterType"] = from_union([from_str, from_none], self.filter_type)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Options"] = from_union(
            [lambda x: from_list(lambda x: to_class(FilterOption, x), x), from_none],
            self.options,
        )
        result["Position"] = from_union([from_int, from_none], self.position)
        result["Rank"] = from_union([from_int, from_none], self.rank)
        return result


@dataclass
class SearchAttribute:
    filters: Optional[List[SearchFilter]] = None
    num_pages: Optional[int] = None
    num_results: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> "SearchAttribute":
        assert isinstance(obj, dict)
        filters = from_union(
            [lambda x: from_list(SearchFilter.from_dict, x), from_none],
            obj.get("Filters"),
        )
        num_pages = from_union([from_int, from_none], obj.get("NumPages"))
        num_results = from_union([from_int, from_none], obj.get("NumResults"))
        return SearchAttribute(filters, num_pages, num_results)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Filters"] = from_union(
            [lambda x: from_list(lambda x: to_class(SearchFilter, x), x), from_none],
            self.filters,
        )
        result["NumPages"] = from_union([from_int, from_none], self.num_pages)
        result["NumResults"] = from_union([from_int, from_none], self.num_results)
        return result


@dataclass
class Taxonomy:
    amazon: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> "Taxonomy":
        assert isinstance(obj, dict)
        amazon = from_union(
            [lambda x: from_list(from_str, x), from_none], obj.get("Amazon")
        )
        return Taxonomy(amazon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Amazon"] = from_union(
            [lambda x: from_list(from_str, x), from_none], self.amazon
        )
        return result


@dataclass
class PageAnnotation:
    all_questions_url: Optional[str] = None
    best_sellers: Optional[BestSellers] = None
    category_overview: Optional[CategoryOverview] = None
    products: Optional[List[Product]] = None
    questions: Optional[List[Question]] = None
    search_attribute: Optional[SearchAttribute] = None
    taxonomy: Optional[Taxonomy] = None

    @staticmethod
    def from_dict(obj: Any) -> "PageAnnotation":
        assert isinstance(obj, dict)
        all_questions_url = from_union(
            [from_str, from_none], obj.get("AllQuestionsURL")
        )
        best_sellers = from_union(
            [BestSellers.from_dict, from_none], obj.get("BestSellers")
        )
        category_overview = from_union(
            [CategoryOverview.from_dict, from_none], obj.get("CategoryOverview")
        )
        products = from_union(
            [lambda x: from_list(Product.from_dict, x), from_none], obj.get("Products")
        )
        questions = from_union(
            [lambda x: from_list(Question.from_dict, x), from_none],
            obj.get("Questions"),
        )
        search_attribute = from_union(
            [SearchAttribute.from_dict, from_none], obj.get("SearchAttribute")
        )
        taxonomy = from_union([Taxonomy.from_dict, from_none], obj.get("Taxonomy"))
        return PageAnnotation(
            all_questions_url,
            best_sellers,
            category_overview,
            products,
            questions,
            search_attribute,
            taxonomy,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["AllQuestionsURL"] = from_union(
            [from_str, from_none], self.all_questions_url
        )
        result["BestSellers"] = from_union(
            [lambda x: to_class(BestSellers, x), from_none], self.best_sellers
        )
        result["CategoryOverview"] = from_union(
            [lambda x: to_class(CategoryOverview, x), from_none], self.category_overview
        )
        result["Products"] = from_union(
            [lambda x: from_list(lambda x: to_class(Product, x), x), from_none],
            self.products,
        )
        result["Questions"] = from_union(
            [lambda x: from_list(lambda x: to_class(Question, x), x), from_none],
            self.questions,
        )
        result["SearchAttribute"] = from_union(
            [lambda x: to_class(SearchAttribute, x), from_none], self.search_attribute
        )
        result["Taxonomy"] = from_union(
            [lambda x: to_class(Taxonomy, x), from_none], self.taxonomy
        )
        return result


@dataclass
class TypesToGenerate:
    page_annotation: PageAnnotation

    @staticmethod
    def from_dict(obj: Any) -> "TypesToGenerate":
        assert isinstance(obj, dict)
        page_annotation = PageAnnotation.from_dict(obj.get("PageAnnotation"))
        return TypesToGenerate(page_annotation)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PageAnnotation"] = to_class(PageAnnotation, self.page_annotation)
        return result


def types_to_generate_from_dict(s: Any) -> TypesToGenerate:
    return TypesToGenerate.from_dict(s)


def types_to_generate_to_dict(x: TypesToGenerate) -> Any:
    return to_class(TypesToGenerate, x)
