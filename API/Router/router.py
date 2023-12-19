from rest_framework import routers

from Analysis.api.ViewsSet import AnalysisViewSet, ReportViewSet
from Brand.api.ViewsSet import BrandViewSet
from Client.api.ViewsSet import ClientViewSet, UserPolymorphicViewSet
from Doctor.api.ViewsSet import DoctorViewSet
from Drug.api.ViewsSet import (
    DrugEffectiveMaterialViewSet,
    DrugPackingViewSet,
    DrugViewSet,
    PharmaceuticalFormViewSet,
)
from Employee.api.ViewsSet import EmployeeViewSet
from Language.api.ViewsSet import LanguageViewSet
from Category.api.ViewsSet import CategoryViewSet
from Currency.api.ViewsSet import CurrencyViewSet
from Address.api.ViewsSet import (
    AddressViewSet,
    CityViewSet,
    CountryViewSet,
    GovernorateViewSet,
    LocalityViewSet,
    StateViewSet,
    StreetViewSet,
)
from Notification.api.ViewsSet import NotificationViewSet
from Radiology.api.ViewsSet import (
    RadiologyImageViewSet,
    RadiologySessionViewSet,
    RadiologyViewSet,
    ServicePolymorphicViewSet,
    ServiceRecordPolymorphicViewSet,
)
from Service.api.ViewsSet import ParentServiceViewSet, ServiceViewSet
from User.api.Views.Avatar_ViewSet import AvatarViewSet
from User.api.Views.Family_ViewSet import FamilyViewSet
from User.api.Views.Profile_ViewSet import ProfileViewSet
from User.api.Views.User_ViewSet import UserViewSet
from Vaccination.api.ViewsSet import (
    CampaignViewSet,
    VaccinationRecordViewSet,
    VaccinationViewSet,
)
from Visit.api.ViewsSet import VisitViewSet, VisitVitalSignViewSet
from VitalSign.api.ViewsSet import VitalSignViewSet
from ..api.ViewsSet import RegisterViewSet

router = routers.DefaultRouter()

# API
router.register("register", RegisterViewSet, basename="register")
# Language
router.register("languages", LanguageViewSet, basename="language")
# Currency
router.register("currencies", CurrencyViewSet, basename="currency")
# Category
router.register("categories", CategoryViewSet, basename="category")
# Address
router.register("address", AddressViewSet, basename="address")
router.register("streets", StreetViewSet, basename="street")
router.register("states", StateViewSet, basename="state")
router.register("localities", LocalityViewSet, basename="locality")
router.register("cities", CityViewSet, basename="city")
router.register("governorates", GovernorateViewSet, basename="governorate")
router.register("countries", CountryViewSet, basename="country")
# Brand
router.register("brands", BrandViewSet, basename="brand")
# User
router.register("users", UserViewSet, basename=UserViewSet.basename)
router.register("families", FamilyViewSet, basename="family")
router.register("profiles", ProfileViewSet, basename="profile")
router.register("avatars", AvatarViewSet, basename="avatar")
# Doctor
router.register("doctors", DoctorViewSet, basename="doctor")
# Employee
router.register("employees", EmployeeViewSet, basename="employee")
# Client
router.register("clients", ClientViewSet, basename="client")
router.register(
    "users_polymorphics", UserPolymorphicViewSet, basename="user_polymorphic"
)
# Service
router.register("services", ServiceViewSet, basename="service")
router.register("parents_services", ParentServiceViewSet, basename="parent_service")
# Notification
router.register("notifications", NotificationViewSet, basename="user")
# Vaccination
router.register("vaccinations", VaccinationViewSet, basename="vaccination")
router.register("campaigns", CampaignViewSet, basename="campaign")
router.register(
    "vaccinations_records", VaccinationRecordViewSet, basename="vaccination_record"
)
# Drug
router.register(
    "pharmaceutical_forms", PharmaceuticalFormViewSet, basename="pharmaceutical_form"
)
router.register(
    "drug_effective_materials",
    DrugEffectiveMaterialViewSet,
    basename="drug_effective_material",
)
router.register("drugs", DrugViewSet, basename="drug")
router.register("drug_packings", DrugPackingViewSet, basename="drug_packing")
# Analysis
router.register("analysis", AnalysisViewSet, basename="analysis")
router.register("reports", ReportViewSet, basename="report")
# VitalSign
router.register("vital_signs", VitalSignViewSet, basename="vital_sign")
# Visit
router.register("visits", VisitViewSet, basename="visit")
router.register(
    "visits_vital_signs", VisitVitalSignViewSet, basename="visit_vital_sign"
)
# Radiology
router.register("radiologies", RadiologyViewSet, basename="radiology")
router.register(
    "radiologies_sessions", RadiologySessionViewSet, basename="radiology_session"
)
router.register("radiologies_images", RadiologyImageViewSet, basename="radiology_image")
router.register(
    "services_polymorphic", ServicePolymorphicViewSet, basename="service_polymorphic"
)
router.register(
    "services_records_polymorphic",
    ServiceRecordPolymorphicViewSet,
    basename="service_record_polymorphic",
)
