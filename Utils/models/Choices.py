from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _
import calendar

# Create your TextChoices here.


class WEEK_DAYS(TextChoices):
    SATURDAY = f"{calendar.SATURDAY}", _("Saturday")
    SUNDAY = f"{calendar.SUNDAY}", _("Sunday")
    MONDAY = f"{calendar.MONDAY}", _("Monday")
    TUESDAY = f"{calendar.TUESDAY}", _("Tuesday")
    WEDNESDAY = f"{calendar.WEDNESDAY}", _("Wednesday")
    THURSDAY = f"{calendar.THURSDAY}", _("Thursday")
    FRIDAY = f"{calendar.FRIDAY}", _("Friday")


class FACILITY_TYPES(TextChoices):
    LABORATORY = "L", _("Laboratory")
    MainLaboratory = "ML", _("MainLaboratory")
    ASSOCIATIONS = "A", _("Association")
    DISPENSARY = "D", _("Dispensary")
    SCIENTIFIC_COMPANY = "SC", _("Scientific Company")
    PHARMACEUTICAL_COMPANY = "Ph", _("Pharmaceutical Company")
    SUPPLYER = "S", _("Supplyer")
    DENTAL_CLINIC = "DC", _("Dental Clinic")
    PRIVATE_CLINIC = "PC", _("Private Clinic")
    GEROCERY = "G", _("Grocery Store")  # بقالة
    BOOK_STORE = "BS", _("Bookstore")  # مكتبة
    COFFEE = "CO", _("Coffee")  # المقهى
    BAKERY = "BA", _("Bakery")  # مخبز
    DELICATESSEN = "DE", _("Delicatessen")  # محل بيع لحوم
    SCHOOL = "Sc", _("School")  # مدرسة
    CAFE = "CA", _("café")  # كافيه
    LAUNDROMAT = "LA", _("Laundromat")  # مغسلة
    HOTAL = "H", _("Hotel")  # الفندق
    BUTCHER = "BU", _("Butcher")  # لجزار
    SUPER_MARKET = "SM", _("SuperMarket ")  # سوبر ماركت
    GIFT_SHOP = "GS", _("Gift Shop")  # محل الهدايا
    FLOWER_SHOP = "FS", _("Flower Shop")  # محل الزهور
    SPORTING_GOODS_STORE = "SG", _("Sporting Goods Store	")  # محل ادوات رياضية
    ELECTRONICS_STORE = "ES", _("Electronics Store")  # محل الكترونيات
    BARBER = "B", _("Barber")
    PHARMACY = "P", _("Pharmacy")
    MEDICAL_FACILITY = "MF", _("Medical Facility")
    MOBILE_NETWORK = "MN", _("Mobile Network Compnay")


class SCORES(TextChoices):
    ONE = "1", _("1")
    TWO = "2", _("2")
    THREE = "3", _("3")


class RUNS(TextChoices):
    SAME_DAY = "SD", _("Same Day")
    NEXT_DAY = "ND", _("Next Day")
    AFTER_2_DAYS = "2D", _("After 2Days")
    AFTER_4_DAYS = "4D", _("After 4Days")
    AFTER_10_DAYS = "10", _("After 10Days")
    AFTER_WEEK = "AW", _("After Week")
    AFTER_2_WEEK = "2W", _("After Two Week")
    AFTER_MONTH = "AM", _("After Month")
    SATURDAY = f"{calendar.SATURDAY}", _("Saturday")
    SUNDAY = f"{calendar.SUNDAY}", _("Sunday")
    MONDAY = f"{calendar.MONDAY}", _("Monday")
    TUESDAY = f"{calendar.TUESDAY}", _("Tuesday")
    WEDNESDAY = f"{calendar.WEDNESDAY}", _("Wednesday")
    THURSDAY = f"{calendar.THURSDAY}", _("Thursday")
    FRIDAY = f"{calendar.FRIDAY}", _("Friday")
    # Saturday = "Sat", _(calendar.day_name[0])
    # Sunday = "Sun", _(calendar.day_name[1])
    # Monday = "Mon", _(calendar.day_name[2])
    # Tuesday = "Tue", _(calendar.day_name[3])
    # Wednesday = "Wed", _(calendar.day_name[4])
    # Thursday = "Thu", _(calendar.day_name[5])
    # Friday = "Fri", _(calendar.day_name[6])


class PERIODIC_TIMES(TextChoices):
    DAILY = "D", _("Daily")
    WEEKLY = "W", _("Weekly")
    MONTHLY = "M", _("Monthly")
    YEARLY = "Y", _("Yearly")


class FINANCIAL_TRANSACTIONS_TYPES(TextChoices):  # أنواع المعاملات المالية
    REVENUES = "R", _("Revenues")  # الإيرادات
    EXPENSES = "E", _("Expenses")  # المصروفات \ نفقات
    # DEBTS = "D", _("Debts")  # مديونيات
    # DUES = "U", _("Dues")  # مستحقات


class PRODUCT_TRANSACTIONS_TYPES(TextChoices):
    IMPORTED_PRODUCTS = "I", _("Imported Products")
    EXPORTED_PRODUCTS = "E", _("Exported Products")


class LOW_OR_NORMAL_OR_HIGH(TextChoices):
    LOW = "L", _("Low")
    NORMAL = "N", _("Normal")
    HIGH = "H", _("High")


class NEGATIVE_OR_POSITIVE(TextChoices):
    NEGATIVE = "N", _("Negative")
    VERY_WEAK_POSITIVE = "VP", _("Very Weak Positive")
    WEAK_POSITIVE = "WP", _("Weak Positive")
    POSITIVE = "P", _("Positive")
    STRONG_POSITIVE = "SP", _("Strong Positive")


class ANALYTICAL_TECHNIQUE_TYPES(TextChoices):
    QUALITATIVE = "Ql", _("Qualitative")
    SEMI_QUANTITATIVE = "SQ", _("Semi Quantitative")
    QUANTITATIVE = "Qn", _("Quantitative")


class PLATFORMS(TextChoices):
    ANDROID = "A", _("Android")
    IOS = "i", _("ios")
    WINDOWS = "W", _("Windows")
    LINUX = "L", _("Linux")
    BROWSER = "B", _("Web Browser")


class DEVICES_TYPES(TextChoices):
    MOBILE = "M", _("Mobile")
    TABLITE = "T", _("Tablete")
    TAB_TOP = "L", _("Lab Top")
    MAC = "P", _("Mac")


class KINSHIP_RELATIONS(TextChoices):
    PARENT = "P", _("Parent")
    CHILD = "C", _("Child")
    SIPLINS = "S", _("Siplins")
    MARIAGE = "M", _("Mariage")


class GRADIENT_TYPES(TextChoices):
    LINEAR_GRADIENT = "LG", _("LinearGradient")


class ALIGMENTS(TextChoices):
    TOP_RIGHT = "TR", _("topRight")
    BOTTOM_LEFT = "BL", _("bottomLeft")
    BOTTOM_RIGHT = "BR", _("bottomRight")
    TOP_LEFT = "TL", _("topRight")


class STATES_TYPES(TextChoices):
    TALUK = "T", _("Taluk")
    VILLAGE = "V", _("Village")  # القرية
    DISTRICT = "D", _("District")  # المنطقة
    MANOR = "M", _("Manor")  # عزبه
    RESIDENTIAL_QUARTER = "RQ", _("Residential Quarter")  # حى سكنى
    HOUSING = "H", _("Housing")  # مساكن
    FEUDALISM = "F", _("Feudalism")  # اقطاعيه
    REGION = "R", _("Region")  # منطقه


class ACTIVITY_TYPES(TextChoices):
    FAVORITE = "F", _("Favorite")
    LIKE = "L", _("Like")
    UP_VOTE = "U", _("Up Vote")
    DOWN_VOTE = "D", _("Down Vote")


class EMPLOYEE_ACTIVITIES(TextChoices):
    PRINT = "P", _("Male")
    DELIVERY = "D", _("Delivery")
    REVIEW = "R", _("Review")
    RECEPTION = "C", _("Recepion")
    CHAT = "H", _("Chat")
    RUN = "U", _("Run")


class GENDERS(TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("FeMale")


class MARITAL_STATUS(TextChoices):
    VIRGIN = "V", _("Virgin")  # اعزب
    BACHELOR = "B", _("Bachelor")  # اعزب
    MARRIED = "M", _("Married")  # متزوج
    WIDOWER = "W", _("Widower")  # ارمل
    DIVORCDE = "D", _("Divorced")  # مطلقه


class JOBS(TextChoices):
    ENGINEAR = "E", _("Engineer")  # مهندس
    DOCTOR = "D", _("doctor")  # طبيب
    TEACHER = "T", _("Teacher")  # مدرس
    PEASANT = "P", _("peasant")  # فلاح
    # BUTCHER = "BU", _("butcher")  # جزار
    # BARBER = "BA", _("barber")  # حلاق
    # CHEMISTIST = "C", _("Chemistry")  # وظيفه كيمياءى
    # HOUSE_WIFE = "HW", _("housewife")  # ربه منزل
    # AUDIOLOGIST = "", _("Audiologist")  #         متخصص السمعيّات
    # ALLERGIST = "", _("Allergist")  #         طبيب متخصص بعلاج الحساسية
    # ANDROLOGISTS = "", _("Andrologists")  #             طبيب امراض الذكورة
    # ANESTHESIOLOGIST = "", _("Anesthesiologist")  #                 طبيب التخدير
    # CARDIOLOGIST = "", _("Cardiologist")  #             طبيب القلب
    # CARDIOVASCULAR_SURGEON = "", _(
    #     "Cardiovascular Surgeon"
    # )  #                     جراح القلب والأوعية الدموية
    # NEUROLOGIST = "", _("Neurologist")  #         طبيب الأعصاب
    # DENTIST = "", _("Dentist")  #     طبيب أسنان
    # DERMATOLOGIST = "", _("Dermatologist")  #             طبيب امراض جلدية
    # EMERGENCY_DOCTORS = "", _("Emergency Doctors")  #                 أطباء الطوارئ
    # ENDOCRINOLOGIST = "", _("Endocrinologist")  #             طبيب الغدد الصماء
    # GASTROENTEROLOGIST = "", _(
    #     "Gastroenterologist"
    # )  #                 طبيب أمراض الجهاز الهضمي
    # GYNECOLOGIST = "", _("Gynecologist")  #             طبيب امراض نساء
    # PSYCHIATRIST = "", _("Psychiatrist")  #             طبيب نفسي
    # HEMATOLOGIST = "", _("Hematologist")  #             طبيب أمراض الدم
    # HEPATOLOGISTS = "", _("Hepatologists")  #             طبيب امراض الكبد
    # IMMUNOLOGIST = "", _("Immunologist")  #             طبيب المناعة
    # INTERNISTS = "", _("Internists")  #         الطبيب الباطني
    # NEONATOLOGIST = "", _("Neonatologist")  #             طبيب حديثي الولادة
    # ORTHOPEDIST = "", _("Orthopedist")  #         طبيب العظام
    # PEDIATRICIAN = "", _("Pediatrician")  #             طبيب الأطفال
    # PLASTIC_SURGEON = "", _("Plastic Surgeon")  #             أخصائي عمليات التجميل
    # SURGEON = "", _("Surgeon")  #     جراح
    # VETERINARIAN = "", _("Veterinarian")  #             طبيب بيطري
    # UROLOGIST = "", _("Urologist")  #         طبيب مسالك بولية
    # RHEUMATOLOGIST = "", _("Rheumatologist")  #             طبيب الروماتيزم


class RESTAURANT_TYPES(TextChoices):
    COFFEE = "C", _("Coffee")
    FAST_FOOD = "F", _("Fast Food")


class SIZES_DEGREE(TextChoices):
    LARGE = "L", _("Large")
    MEDIUM = "M", _("Medium")
    SMALL = "S", _("Small")


class MEDICAL_SPECIALTIES(TextChoices):
    INTERNAL_MEDICINE = "IM", _("Internal Medicine")  #     الطب الباطني
    NEPHROLOGY = "N", _("Nephrology")  # تخصص أمراض الكلى
    NEUROLOGY = "NR", _("Neurology ")  # طب تخصص أعصاب
    OBSTETRICS_AND_GYNECOLOGY = "OG", _(
        "Obstetrics & Gynecology"
    )  #  طب تخصص النساء والتوليد
    # ONCOLOGY = "", _("Oncology")  # تخصص الأورام
    # OPHTHALMOLOGY = "", _("Ophthalmology")  # طب العيون
    # ORTHOPEDICS = "", _("Orthopedics")  # طب تخصص العظام
    # PEDIATRICS = "", _("Pediatrics")  # طب الأطفال
    # PLASTIC_SURGERY = "", _("Plastic surgery")  # جراحة التجميل
    # PSYCHIATRY = "", _("Psychiatry")  # طب الأمراض النفسية
    # RHEUMATOLOGY = "", _("Rheumatology")  # طب أمراض الروماتيزم
    # UROLOGY = "", _("Urology")  #    طب أمراض المسالك البولية
    # VETERINARY_MEDICINE = "", _("Veterinary medicine")  #
    # ANATOMY = "", _("Anatomy")  # التشريح
    # ANESTHESIA = "", _("Anesthesia")  #    التخدير
    # CARDIOLOGY = "", _("Cardiology")  #  طب القلب
    # CARDIAC_SURGERY = "", _("Cardiac Surgery")  #   جراحة القلب
    # DENTISTRY = "", _("Dentistry ")  #    طب الأسنان
    # DERMATOLOGY = "", _("Dermatology")  #    أمراض جلدية
    # EAR_NOSE_AND_THROAT = "ENT", _("Ear, nose and throat")  #  طب الأنف والأذن والحنجرة
    # ENDOCRINOLOGY = "", _("Endocrinology")  # طب تخصص الغدد
    # GASTROENTEROLOGY = "", _("Gastroenterology")  # طب أمراض الجهاز الهضمي
    # GENERAL_SURGERY = "", _("General surgery")  # الجراحة العامة
    # HEMATOLOGY = "", _("Hematology")  #    أمراض الدم
    # HEPATOLOGY = "", _("Hepatology")  #    طب أمراض الكبد
    # SPORTS_MEDICINE = "", _("Sports medicine")  #           الطب الرياضي
    # PEDIATRIC_RADIOLOGY = "", _("Pediatric radiology")  #               أشعة أطفال
    # LIVER_TRANSPLANT_SURGERY = "", _(
    #     "Liver Transplant Surgery"
    # )  #                       تخصص زراعة الكبد
    # PSYCHOSOMATIC_MEDICINE = "", _(
    #     "Psychosomatic medicine"
    # )  #                   الطب النفسي الجسدي
    # PEDIATRIC_SURGERY = "", _("Pediatric surgery")  #               جراحة الأطفال
    # GENETIC_PATHOLOGY = "", _(
    #     "Genetic pathology"
    # )  #               علم الأمراض المرتبط بالجينات الوراثية
    # HOSPICE_AND_PALLIATIVE_MEDICINE = "", _(
    #     "Hospice and palliative medicine"
    # )  #       رعاية المحتضرين و الطب التلطيفي
    # MOLECULAR_GENETIC_PATHOLOGY = "", _(
    #     "Molecular genetic pathology"
    # )  #                       علم الأمراض المرتبط بالجينات الوراثية
    # FOOT_AND_ANKLE_ORTHOPEDICS = "", _(
    #     "Foot and ankle orthopedics"
    # )  #                       جراحة عظام القدم و الكاحل
    # NEURO_OPHTHALMOLOGY = "", _("Neuro-ophthalmology")  #               طب أعصاب العيون
    # CHILD_ABUSE_PEDIATRICS = "", _(
    #     "Child abuse pediatrics"
    # )  #                   طب الأطفال الخاص بإساءة الأطفال
    # OCCUPATIONAL_MEDICINE = "", _(
    #     "Occupational medicine"
    # )  #                   الطب المهني
    # SURGERY = "", _("Surgery ")  #  راحة
    # FORENSIC_PSYCHIATRY = "", _(
    #     "Forensic psychiatry"
    # )  #               الطب النفسي الشرعي
    # PEDIATRIC_GASTROENTEROLOGY = "", _(
    #     "Pediatric gastroenterology"
    # )  #                       طب الأطفال الخاص بأمراض الجهاز الهضمي
    # COLON_AND_RECTAL_SURGERY = "", _(
    #     "Colon and rectal surgery"
    # )  #                       جراحة القولون و المستقيم
    # CARDIO_THORACIC_SURGERY = "", _(
    #     "Cardio thoracic surgery "
    # )  #                   جراحة القلب و الصدر
    # ADOLESCENT_MEDICINE = "", _("Adolescent medicine")  #               طب المراهقين
    # RECONSTRUCTIVE_ORTHOPEDICS = "", _(
    #     "Reconstructive orthopedics"
    # )  #                       جراحة العظام الترميمية
    # VASCULAR_AND_INTERVENTIONAL_RADIOLOGY = "", _(
    #     "Vascular and interventional radiology"
    # )  #              الأشعة الوعائية و التداخلية
    # MEDICINE_OF_INFECTIOUS_DISEASES = "", _(
    #     "Medicine of infectious diseases"
    # )  #      طب الأمراض المعدية
    # NEUROPATHOLOGY = "", _("Neuropathology ")  #           علم الأمراض العصبية
    # IMMUNOPATHOLOGY = "", _("Immunopathology")  #           الأمراض المناعية
    # PAI_MANAGEMENT_MEDICINE = "", _(
    #     "Pain management medicine"
    # )  #                       طب علاج الألم
    # SPINAL_CORD_INJURY_MEDICINE = "", _(
    #     "Spinal cord injury medicine"
    # )  #                       طب إصابات الحبل الشوكي
    # # CARDIOLOGY      = "", _("Cardiology ")   #       طب أمراض القلب
    # RADIATION_ONCOLOGY = "", _(
    #     "Radiation oncology "
    # )  #               طب علاج الأورام بالإشعاع
    # BLOOD_BANKING_AND_TRANSFUSION_MEDICINE = "", _(
    #     "Blood banking and transfusion medicine  "
    # )  #           طب بنوك الدم و نقله
    # ORTHOPEDIC_SPORTS_MEDICINE = "", _(
    #     "Orthopedic sports medicine"
    # )  #                       طب العظام الرياضي
    # FORENSIC_PATHOLOGY = "", _(
    #     "Forensic pathology "
    # )  #               علم الأمراض الشرعي
    # # HEMATOLOGY      = "", _("Hematology ")   #       علم أمراض الدم
    # ANESTHESIOLOGY = "", _("Anesthesiology ")  #           طب التخدير
    # CRITICAL_CARE_MEDICINE = "", _(
    #     "Critical care medicine"
    # )  #                   طب الرعاية الحرجة
    # CHEMICAL_PATHOLOGY = "", _(
    #     "Chemical pathology "
    # )  #               علم الأمراض الكيميائي
    # ABDOMINAL_RADIOLOGY = "", _(
    #     "Abdominal radiology"
    # )  #               أشعة الجهاز الهضمي
    # MUSCULOSKELETAL_RADIOLOGY = "", _(
    #     "Musculoskeletal radiology "
    # )  #                       أشعة الجهاز العضلي الهيكلي
    # PEDIATRIC_ONCOLOGY = "", _("Pediatric oncology ")  #               طب أورام الأطفال
    # PEDIATRIC_PULMONOLOGY = "", _(
    #     "Pediatric pulmonology"
    # )  #                   طب الأمراض التنفسية للأطفال
    # RENAL_TRANSPLANT_SURGERY = "", _(
    #     "Renal transplant surgery"
    # )  #                       جراحة زراعة الكلى
    # LIAISON_PSYCHIATRY = "", _(
    #     "Liaison psychiatry "
    # )  #               الطب النفسي الوصلي
    # HAND_SURGERY = "", _("Hand surgery")  #           جراحة اليد
    # MEDICAL_GENETICS = "", _("Medical genetics")  #               علم الوراثة الطبية
    # SLEEP_MEDICINE = "", _("Sleep medicine ")  #           طب أمراض النوم
    # PEDIATRIC_OTOLARYNGOLOGY = "", _(
    #     "Pediatric otolaryngology"
    # )  #                       طب الأذن والأنف والحنجرة للأطفال
    # ORTHOPEDIC_SURGERY = "", _("Orthopedic surgery ")  #               جراحة العظام
    # MUSCULOSKELETAL = "", _(
    #     "Musculoskeletal"
    # )  #           oncology طب أورام الجهاز العضلي الهيكلي
    # NEUROSURGERY = "", _("Neurosurgery")  #           جراحة المخ و الأعصاب
    # NUCLEAR_MEDICINE = "", _("Nuclear medicine")  #               الطب النووي
    # UROLOGIC_ONCOLOGY = "", _("Urologic oncology")  #               طب أورام المسالك
    # PATHOLOGY = "", _("Pathology")  #       علم الأمراض
    # NEURORADIOLOGY = "", _("Neuroradiology ")  #           أشعة الجهاز العصبي
    # EMERGENCY_MEDICINE = "", _("Emergency Medicine ")  #               طب الطواريء
    # ADDICTION_PSYCHIATRY = "", _(
    #     "Addiction psychiatry"
    # )  #                   الطب النفسي لعلاج الإدمان
    # PEDIATRIC_CARDIOLOGY = "", _(
    #     "Pediatric cardiology"
    # )  #                   طب أمراض القلب للأطفال
    # PEDIATRIC_ANESTHESIOLOGY = "", _(
    #     "Pediatric anesthesiology"
    # )  #                       طب التخدير للأطفال
    # # OBSTETRICS_AND_GYNECOLOGY                         = "", _("Obstetrics and gynecology ")   #                       طب النساء و التوليد
    # PEDIATRIC_ORTHOPEDICS = "", _(
    #     "Pediatric orthopedics"
    # )  #                   جراحة العظام للأطفال
    # # ONCOLOGY        = "", _("Oncology")   #       طب الأورام
    # ORAL_AND_MAXILLOFACIAL_SURGERY = "", _(
    #     "Oral and maxillofacial surgery "
    # )  #    جراحة الفم و الوجه و الفكين
    # GASTROINTESTINAL_RADIOLOGY = "", _(
    #     "Gastrointestinal radiology"
    # )  #                       أشعة الجهاز الهضمي
    # DIAGNOSTIC_RADIOLOGY = "", _(
    #     "Diagnostic radiology"
    # )  #                   الأشعة التشخيصية
    # GLAUCOMA_OPHTHALMOLOGY = "", _(
    #     "Glaucoma ophthalmology"
    # )  #                   طب العيون لمرض الماء الزرقاء
    # GERIATRI_MEDICINE = "", _("Geriatric medicine ")  #               طب كبار السن
    # TRAUMA_MEDICINE = "", _("Trauma Medicine")  #           طب الإصابات و الحوادث
    # FAMILY_MEDICINE = "", _("Family medicine")  #           طب الأسرة
    # PEDIATRIC_EMERGENCY_MEDICINE = "", _(
    #     "Pediatric emergency medicine"
    # )  #       طب طوارئ الأطفال
    # PEDIATRIC_DERMATOLOGY = "", _(
    #     "Pediatric dermatology"
    # )  #                   طب جلدية الأطفال
    # PEDIATRIC_NEPHROLOGY = "", _(
    #     "Pediatric nephrology"
    # )  #                   طب كلى الأطفال
    # MEDICAL_TOXICOLOGY = "", _("Medical toxicology ")  #               طب السموم
    # # NEUROLOGY       = "", _("Neurology")   #       طب الأمراض العصبية
    # OPHTHALMIC_SURGERY = "", _("Ophthalmic surgery ")  #               جراحة العيون
    # # GENERAL_SURGERY = "", _("General surgery")   #           الجراحة العامة
    # PEDIATRIC_UROLOGY = "", _("Pediatric urology")  #               طب مسالك الأطفال
    # GERIATRIC_PSYCHIATRY = "", _(
    #     "Geriatric psychiatry"
    # )  #                   الطب النفسي لكبار السن
    # INTERVENTIONAL_CARDIOLOGY = "", _(
    #     "Interventional cardiology "
    # )  #                       الطب التداخلي لأمراض القلب
    # CYTOPATHOLOGY = "", _("Cytopathology")  #           علم الأمراض الخلوي
    # # PSYCHIATRY      = "", _("Psychiatry ")   #       الطب النفسي
    # AEROSPACE_MEDICINE = "", _("Aerospace medicine ")  #               طب الفضاء
    # NEUROMUSCULAR_MEDICINE = "", _(
    #     "Neuromuscular medicine"
    # )  #                   الطب العصبي العضلي
    # HEAD_AND_NECK_RADIOLOGY = "", _(
    #     "Head and neck radiology "
    # )  #                   أشعة الرأس والرقبة
    # REPRODUCTIVE_ENDOCRINOLOGY_AND_INFERTILITY = "", _(
    #     "Reproductive endocrinology and infertility"
    # )  #            طب الغدد الصماء التناسلية و العقم
    # # RHEUMATOLOGY    = "", _("Rheumatology")   #           الروماتيزم
    # # GASTROENTEROLOGY= "", _("Gastroenterology")   #               طب الجهاز الهضمي
    # OPHTHALMIC_PLASTIC_amp_RECONSTRUCTIVE_SURGERY = "", _(
    #     "Ophthalmic Plastic & Reconstructive Surgery"
    # )  #       جراحة العيون التجميلية والترميمية
    # CONGENITAL_CARDIAC_SURGERY = "", _(
    #     "Congenital cardiac surgery"
    # )  #                       جراحة العيوب الخلقية للقلب
    # ALLERGY_AND_IMMUNOLOGY = "", _(
    #     "Allergy and immunology"
    # )  #                   الحساسية و المناعة
    # # DERMATOLOGY     = "", _("Dermatology")   #       الجلدية
    # GYNECOLOGIC_ONCOLOGY = "", _(
    #     "Gynecologic oncology"
    # )  #                   أورام النساء
    # CLINICAL_PATHOLOGY = "", _(
    #     "Clinical pathology "
    # )  #               علم الأمراض السريري
    # GENITOURINARY_RADIOLOGY = "", _(
    #     "Genitourinary radiology "
    # )  #                   أشعة المسالك البولية
    # FEMALE_UROLOGY = "", _(
    #     "Female urology "
    # )  #           جراحة المسالك البولية الأنثوية
    # PEDIATRIC_TRANSPLANT_HEPATOLOGY = "", _(
    #     "Pediatric transplant hepatology"
    # )  #      زراعة الكبد للأطفال
    # PEDIATRIC_ENDOCRINOLOGY = "", _(
    #     "Pediatric endocrinology "
    # )  #                   طب الغدد الصماء للأطفال
    # CRANIOFACIAL_SURGERY = "", _(
    #     "Craniofacial surgery"
    # )  #                   جراحة الرأس و الوجه
    # PEDIATRIC_OPHTHALMOLOGY = "", _(
    #     "Pediatric ophthalmology "
    # )  #                   طب العيون للأطفال
    # INTERVENTIONAL_RADIOLOGY = "", _(
    #     "Interventional radiology"
    # )  #                       الأشعة التداخلية
    # PHYSICAL_MEDICINE_AND_REHABILITATION = "", _(
    #     "Physical medicine and rehabilitation"
    # )  #      العلاج الطبيعي و إعادة التأهيل
    # MILITARY_PSYCHIATRY = "", _(
    #     "Military psychiatry"
    # )  #               الطب النفسي العسكري
    # CHEST_RADIOLOGY = "", _("Chest radiology")  #           أشعة الصدر
    # CHILD_NEUROLOGY = "", _("Child neurology")  #           طب الأعصاب للأطفال
    # PREVENTIVE_MEDICINE = "", _("Preventive medicine")  #               الطب الوقائي
    # PEDIATRIC_HEMATOLOGY_ONCOLOGY = "", _(
    #     "Pediatric hematology-oncology"
    # )  #    أمراض الدم والأورام لدى الأطفال
    # BIOCHEMICAL_GENETICS = "", _(
    #     "Biochemical genetics"
    # )  #                   علم الوراثة البيوكيميائية
    # EMERGENCY_RADIOLOGY = "", _("Emergency radiology")  #               أشعة الطوارئ
    # CHILD_AND_ADOLESCENT_PSYCHIATRY = "", _(
    #     "Child and adolescent psychiatry"
    # )  #     الطب النفسي للأطفال والمراهقين
    # # PLASTIC_SURGERY = "", _("Plastic surgery")   #           جراحة التجميل
    # CLINICAL_NEUROPHYSIOLOGY = "", _(
    #     "Clinical neurophysiology"
    # )  #                       الفسيولوجيا العصبية السريرية
    # SURGICAL_CRITICAL_CARE = "", _(
    #     "Surgical critical care"
    # )  #                   الرعاية الحرجة الجراحية
    # ADVANCED_HEART_FAILURE_AND_TRANSPLANT_CARDIOLOGY = "", _(
    #     "Advanced heart failure and transplant cardiology "
    # )  #       طب قصور القلب المتقدم وزراعة القلب
    # VASCULAR_SURGERY = "", _("Vascular surgery")  #               جراحة الأوعية الدموية
    # DEVELOPMENTAL_BEHAVIORAL_PEDIATRICS = "", _(
    #     "Developmental-behavioral pediatrics "
    # )  #                          طب الأطفال السلوكي النمائي
    # # UROLOGY         = "", _("Urology ")   #  حة المسالك البولية
    # # NEPHROLOGY      = "", _("Nephrology ")   #       طب الكلى
    # OCULAR_ONCOLOGY = "", _("Ocular oncology")  #           أورام العيون
    # PUBLIC_HEALTH_MEDICINE = "", _(
    #     "Public health medicine"
    # )  #                   طب الصحة العامة
    # EMERGENCY_PSYCHIATRY = "", _(
    #     "Emergency psychiatry"
    # )  #                   طواريء الطب النفسي
    # NEONATAL_PERINATAL_MEDICINE = "", _(
    #     "Neonatal-perinatal medicine"
    # )  #        طب حديثي الولادة في الفترة المحيطة بالولادة
    # PEDIATRIC_INFECTIOUS_DISEASES = "", _(
    #     "Pediatric infectious diseases"
    # )  #      الأمراض المعدية للأطفال
    # MATERNAL_FETAL_MEDICINE = "", _(
    #     "Maternal-fetal medicine "
    # )  #            طب الأم والجنين
    # CARDIOTHORACIC_RADIOLOGY = "", _(
    #     "Cardiothoracic radiology"
    # )  #            أشعة القلب والصدر
    # OTOLARYNGOLOGY = "", _("Otolaryngology ")  #           طب الأنف والأذن والحنجرة
    # MEDICAL_MICROBIOLOGY = "", _(
    #     "Medical microbiology"
    # )  #                   علم الأحياء الدقيقة الطبية
    # # PEDIATRICS      = "", _("Pediatrics ")   #       طب الأطفال
    # CARDIOVASCULAR_RADIOLOGY = "", _(
    #     "Cardiovascular radiology"
    # )  #          أشعة القلب والأوعية الدموية
    # PEDIATRIC_REHABILITATION_MEDICINE = "", _(
    #     "Pediatric rehabilitation medicine"
    # )  #          طب إعادة تأهيل الأطفال
    # COMMUNITY_PSYCHIATRY = "", _("Community psychiatry")  #       الطب النفسي المجتمعي


"""
        طب الباطنة	Internal Medicine
        باطنة غدد صماء وسكر	Endocrinology
        القلب والاوعية الدموية	Cardiology
        باطنة جهاز هضمي ومناظير	Gastroenterology
        نساء وتوليد	Obstetrics and Gynecology
        طب العيون	Ophthalmology
        طب اطفال	Pediatrics
        طب الانف والاذن والحنجرة	(Ear, nose and throat (ENT
        طب امراض العيون	Ophthalmology
        طب الاعصاب	Neurology
        طب امراض الكلى	nephrology
        طب الاورام	Oncology
        المسالك البولية	Urology
        جلدية	Dermatology
        طب الاورام	Oncology
        الحساسية والمناعة	Allergy and immunology
        امراض الدم	Hematology
        الطب العام	General Practitioner
        طب الطوارىء	Emergency medicine

        طب الامراض النفسية	Psychiatry
        الاشعة	Radiology
        طب الاسنان	Dentistry
        طب التشريح	Anatomy
        طب الغدد	Endocrinology
        طب الاسرة	Family medicine
        الطب الرياضي	Sports medicine
        طب الامراض المهنية	Industrial medicine
        الطب الوقائى	Preventative medicine
        طب التخدير	Anesthesia
        طب امراض الروماتيزم	Rheumatology
        طب امراض الكبد	Hepatology
        طب التخدير والانعاش	Anesthesiology & Recovery
        الطب الشرعي	Forensic Medicine
        طب المناطق الحارة	Tropical  Medicine
        الطب النووي	Nuclear Medicine
        التخاطب	Speech-Language
        طب الفضاء	Space  Medicine
        طب بيطري	veterinary science

        الجراحة	surgery
        الجراحة العامة	General Surgery
        جراحة الأطفال	Pediatric surgery
        جراحة التجميل	plastic surgery
        جراحة المسالك البولية	Urology surgery
        جراحة الاعصاب	Neurosurgery
        جراحة القلب	Cardiac surgery
        جراحة الاوعية الدموية	Vascular surgery
        جلراحة عظام	Orthopedics
        جراحة انف و أذن وحنجرة	Ear, nose and throat (ENT) surgery
        جراحة الاورام	Oncology
        جراحة الصدر	Thoracic surgery
        جراحة المخ	brain surgery
        جراحة الشرج	anal surgery
        جراحة عامة	General Surgery
        جراحة بدون نزيف	bloodless surgery
        جراحة بنائية	Reconstructive
        جراحة صغرى	minor surgery
        جراحة كبرى	major surgery
"""  # https://learnenglish.nu/english-learning-language.php?english-learning=214
# https://www.englishtools.org/ar/convert-sentences-case-uppercase-lowercase
# https://learnenglish.nu/english-dictionary.php?english=types-of-doctors-%D8%A7%D8%B3%D9%85%D8%A7%D8%A1-%D8%A7%D9%84%D8%A3%D8%B7%D8%A8%D8%A7%D8%A1-%D8%AD%D8%B3%D8%A8-%D8%A7%D9%84%D8%A7%D8%AE%D8%AA%D8%B5%D8%A7%D8%B5%D8%A7%D8%AA-%D8%A8%D8%A7%D9%84%D9%84%D8%BA%D8%A9-%D8%A7%D9%84%D8%A7%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A%D8%A9-%D9%85%D8%B9-%D8%A7%D9%84%D9%84%D9%81%D8%B8-%D9%88%D8%A7%D9%84%D8%AA%D8%B1%D8%AC%D9%85%D8%A9&id=68


class UNIT_PREFIXES(TextChoices):
    QUETTA = "Q", _("Quetta")
    # QUETTA = "R", _("Ronna")
    # QUETTA = "Y", _("Yotta")
    # QUETTA = "Z", _("Zetta")
    # QUETTA = "E", _("Exa")
    # QUETTA = "P", _("Peta")
    # QUETTA = "T", _("Tera")
    # QUETTA = "G", _("Giga")
    # QUETTA = "M", _("Mega")
    # QUETTA = "K", _("Kilo")
    # QUETTA = "h", _("Hecto")
    # QUETTA = "da", _("Deca")
    # _ = "", _("")
    # QUETTA = "d", _("Deci")
    # QUETTA = "c", _("Centi")
    # QUETTA = "m", _("Milli")
    # QUETTA = "μ", _("Micro")
    # QUETTA = "n", _("Nano")
    # QUETTA = "p", _("Pico")


class UNIT(TextChoices):
    Mg_dl = "m", _("mg/dL.")
    # QUETTA = "R", _("Ronna")
    # QUETTA = "Y", _("Yotta")
    # QUETTA = "Z", _("Zetta")
    # QUETTA = "E", _("Exa")
    # QUETTA = "P", _("Peta")
