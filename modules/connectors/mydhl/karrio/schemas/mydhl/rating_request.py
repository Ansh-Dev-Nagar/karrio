import attr
import jstruct
import typing


@attr.s(auto_attribs=True)
class AccountType:
    typeCode: typing.Optional[str] = None
    number: typing.Optional[int] = None


@attr.s(auto_attribs=True)
class ErDetailsType:
    postalCode: typing.Optional[str] = None
    cityName: typing.Optional[str] = None
    addressLine1: typing.Optional[str] = None
    addressLine2: typing.Optional[str] = None
    countryCode: typing.Optional[str] = None
    addressLine3: typing.Optional[str] = None


@attr.s(auto_attribs=True)
class CustomerDetailsType:
    shipperDetails: typing.Optional[ErDetailsType] = jstruct.JStruct[ErDetailsType]
    receiverDetails: typing.Optional[ErDetailsType] = jstruct.JStruct[ErDetailsType]


@attr.s(auto_attribs=True)
class EstimatedDeliveryDateType:
    isRequested: typing.Optional[bool] = None
    typeCode: typing.Optional[str] = None


@attr.s(auto_attribs=True)
class MonetaryAmountType:
    typeCode: typing.Optional[str] = None
    value: typing.Optional[int] = None
    currency: typing.Optional[str] = None


@attr.s(auto_attribs=True)
class DimensionsType:
    length: typing.Optional[int] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None


@attr.s(auto_attribs=True)
class PackageType:
    typeCode: typing.Optional[str] = None
    weight: typing.Optional[int] = None
    dimensions: typing.Optional[DimensionsType] = jstruct.JStruct[DimensionsType]


@attr.s(auto_attribs=True)
class ProductsAndServiceType:
    productCode: typing.Optional[str] = None
    localProductCode: typing.Optional[str] = None


@attr.s(auto_attribs=True)
class RatingRequestType:
    customerDetails: typing.Optional[CustomerDetailsType] = jstruct.JStruct[CustomerDetailsType]
    accounts: typing.Optional[typing.List[AccountType]] = jstruct.JList[AccountType]
    productsAndServices: typing.Optional[typing.List[ProductsAndServiceType]] = jstruct.JList[ProductsAndServiceType]
    payerCountryCode: typing.Optional[str] = None
    plannedShippingDateAndTime: typing.Optional[str] = None
    unitOfMeasurement: typing.Optional[str] = None
    isCustomsDeclarable: typing.Optional[bool] = None
    monetaryAmount: typing.Optional[typing.List[MonetaryAmountType]] = jstruct.JList[MonetaryAmountType]
    estimatedDeliveryDate: typing.Optional[EstimatedDeliveryDateType] = jstruct.JStruct[EstimatedDeliveryDateType]
    getAdditionalInformation: typing.Optional[typing.List[EstimatedDeliveryDateType]] = jstruct.JList[EstimatedDeliveryDateType]
    returnStandardProductsOnly: typing.Optional[bool] = None
    nextBusinessDay: typing.Optional[bool] = None
    productTypeCode: typing.Optional[str] = None
    packages: typing.Optional[typing.List[PackageType]] = jstruct.JList[PackageType]
