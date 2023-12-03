from rest_framework import routers

from API.api.Serializers.Password import ChangePasswordSerializer
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
from User.api.Views.family_views_set import FamilyViewSet
from User.api.Views.user_views_set import UserViewSet
from User.api.Views.profile_views_set import ProfileImageViewSet, ProfileViewSet
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
router.register("languages", LanguageViewSet)
# Currency
router.register("currencies", CurrencyViewSet)
# Category
router.register("categories", CategoryViewSet)
# Address
router.register("address", AddressViewSet)
router.register("street", StreetViewSet)
router.register("states", StateViewSet)
router.register("localities", LocalityViewSet)
router.register("cities", CityViewSet)
router.register("governorates", GovernorateViewSet)
router.register("countries", CountryViewSet)
# Brand
router.register("brands", BrandViewSet)
# User
router.register("users", UserViewSet)
router.register("families", FamilyViewSet)
router.register("profiles", ProfileViewSet)
router.register("profiles_images", ProfileImageViewSet)
# Doctor
router.register("doctors", DoctorViewSet)
# Employee
router.register("employees", EmployeeViewSet)
# Client
router.register("clients", ClientViewSet)
router.register("users_polymorphic", UserPolymorphicViewSet)
# Service
router.register("services", ServiceViewSet)
router.register("parents_services", ParentServiceViewSet)
# Notification
router.register("notifications", NotificationViewSet)
# Vaccination
router.register("vaccinations", VaccinationViewSet)
router.register("campaigns", CampaignViewSet)
router.register("vaccinations_records", VaccinationRecordViewSet)
# Drug
router.register("pharmaceutical_forms", PharmaceuticalFormViewSet)
router.register("drug_effective_materials", DrugEffectiveMaterialViewSet)
router.register("drugs", DrugViewSet)
router.register("drug_packings", DrugPackingViewSet)
# Analysis
router.register("analysis", AnalysisViewSet)
router.register("reports", ReportViewSet)
# VitalSign
router.register("vital_signs", VitalSignViewSet)
# Visit
router.register("visits", VisitViewSet)
router.register("visits_vital_signs", VisitVitalSignViewSet)
# Radiology
router.register("radiologies", RadiologyViewSet)
router.register("radiologies_sessions", RadiologySessionViewSet)
router.register("radiologies_images", RadiologyImageViewSet)
router.register("services_polymorphic", ServicePolymorphicViewSet)
router.register("services_records_polymorphic", ServiceRecordPolymorphicViewSet)
