from enum import Enum

class LifeSituationName(Enum):
    MULTICHILD_FAMILY = 'Многодетная семья'
    INDIVIDUAL_HOUSE_CONSTRUCTION = 'Строительство индивидуального жилого дома'
    EMERGENCY_SITUATION = 'Попадание в чрезвычайную ситуацию'
    UNIVERSITY_ADMISSION = 'Поступление в ВУЗ'
    JOB_SEARCH = 'Поиск работы (в том числе для молодых специалистов)'
    BUSINESS_SUPPORT = 'Получение мер поддержки для развития бизнеса'
    PRODUCT_LAUNCH = 'Выпуск продукции в оборот и/или продажу'
    GRAIN_AGRICULTURE = 'Развитие бизнеса зерновой отрасли растениеводства (КФХ)'
    LOGISTICS_ORGANIZATION = 'Организация логистики грузов (за пределы РФ)'
    TOURISM_OBJECT_OPENING = 'Открытие туристического объекта (в том числе для лечения (оздоровления) и отдыха)'
    TOURISM_TRIPS_ORGANIZATION = 'Организация туристических поездок'
    PRIVATE_SCHOOL_OR_KINDERGARTEN_OPENING = 'Открытие частной школы/детского сада'
    PHARMACY_OPENING = 'Открытие аптеки'
    RADIO_STATION_OPENING = 'Открытие радиостанции'
    REAL_ESTATE_AGENCY_OPENING = 'Открытие риэлторского агентства'
    ALCOHOL_PRODUCTION_COMPANY_OPENING = 'Открытие предприятия по производству алкогольной продукции'
    TOURISM_COMPANY_OPENING = 'Открытие туристической компании'
    JEWELRY_MANUFACTURING_OPENING = 'Открытие ювелирного производства'
    SMALL_SHIP_PURCHASE = 'Приобретение маломерного судна для некоммерческого пользования'
    AIRCRAFT_PILOT_LICENSE = 'Получение права на управление летным транспортным средством'
    MASS_SPORTS_OBJECTS_CREATION = 'Создание (реконструкция) объектов массового спорта с применением механизмов государственного-частного партнерства и предоставлении физкультурного-оздоровительных услуг населению на основе спроса'
    PUBLIC_SERVICE_EMPLOYMENT = 'Приём сотрудников на государственную службу'
    CIVIL_SERVICE_EMPLOYMENT_TERMINATION = 'Увольнение сотрудников с государственной гражданской службы'
    HUNTING_AND_FISHING_TRIP = 'Выезд на охоту и рыбалку'
    AMATEUR_SPORTS_PARTICIPATION = 'Участие в спортивных (любительских) соревнованиях'
    PHYSICAL_HARM_TO_OTHER = 'Причинение физического вреда/травмы другому человеку'
    EARLY_UNIVERSITY_EDUCATION_SUSPENSION = 'Досрочное приостановление обучения в университете'
    INCARCERATION = 'Пребывание в месте лишения свободы'
    CHILD_PLACEMENT_IN_CARE_OR_ADOPTION = 'Передача своего ребёнка в органы опеки или на усыновление в интернат'
    ADMINISTRATIVE_PUNISHMENT = 'Получение административного наказания'
    TRAFFIC_ACCIDENT = 'Участие в ДТП'
    CAREER_ORIENTATION_TEST_TAKING = 'Прохождение теста на профориентацию'
    CAREER_ORIENTATION_TEST_RECEIVING = 'Получение теста на профориентацию'
    PSYCHOLOGICAL_DISORDER_DIAGNOSIS = 'Получение диагноза психологического отклонения/расстройства'
    SUBSTANCE_ABUSE_TREATMENT = 'Прохождение лечения зависимостей (наркомания, алкоголизм и др.)'
    BUSINESS_CLOSURE = 'Закрытие своего бизнеса'
    PET_OWNERSHIP = 'Завёл домашнее животное'
    VOLUNTARY_EMPLOYMENT_TERMINATION = 'Увольнение по собственному желанию'
    EMPLOYMENT_AFTER_DISABILITY = 'Трудовая деятельность после получения инвалидности'
    TROUBLED_FAMILY_STATUS_RECOGNITION = 'Признание государством семьи с детьми неблагополучной'
    CRIMINAL_SENTENCE = 'Получение уголовного наказания'
    POST_RETIREMENT_EMPLOYMENT = 'Трудовая деятельность после выхода на пенсию'
    PROLONGED_INABILITY = 'Продолжительная (более полугода) недееспособность (зависимость от других людей или нужна в домашнем уходе)'
    ARMY_CONSCRIPTION_OR_SERVICE = 'Призыв или служба в армии'
    CHILD_ADOPTION_PLANNING = 'Планирование усыновление ребёнка'
    DEEP_DEPRESSION = 'Находился(лас) в состоянии глубокой депрессии более недели'
    LONELINESS_EXTENDED_DURATION = 'Испытывал чувство одиночества длительное время (более 6 месяцев)'
    VOLUNTEER_WORK_PARTICIPATION = 'Участие в волонтёрской деятельности'
    LONG_TERM_UNEMPLOYMENT = 'Длительная безработица (более 6 месяцев)'
    FORCED_RELOCATION = 'Вынужденный переезд'
    MARRIAGE_DISSOLUTION = 'Расторжение брака'
    BUSINESS_AFTER_RETIREMENT = 'Трудовая деятельность после выхода на пенсию'
    BUSINESS_ESTABLISHMENT = 'Открытие своего бизнеса'
    BULLYING_OR_PSYCHOLOGICAL_HARASSMENT = 'Длительное время подвергался травле или психологическим издевательствам'
    ABORTION_FOR_MEDICAL_REASONS = 'Аборт(ы) по медицинским показателям'
    FAMILY_VIOLENCE = 'Насилие в семье'
    MILITARY_COMBAT_SERVICE = 'Участие в боевых действиях на фронте'
    CAREER_RETRAINING = 'Переобучение для работы по другой специальности'
    JOB_LOSS = 'Потеря работы (сокращение или увольнение)'
    DOMESTIC_RELOCATION = 'Переезд внутри страны'
    DRIVERS_LICENSE_ACQUISITION = 'Получение водительских прав'
    OFFICIAL_DISABILITY_STATUS = 'Получение официального статуса инвалида'
    CHILD_WITH_DISABILITY_EDUCATION = 'Обучение ребёнка с инвалидностью'
    BREADWINNER_LOSS = 'Потеря кормильца'
    ELDERLY_CARE = 'Уход за престарелым'
    CAR_PURCHASE_AND_REGISTRATION = 'Покупка и поставка автомобиля на учёт'
    MORTGAGE_OR_LARGE_LOAN_ACQUISITION = 'Получение ипотеки/крупного кредита'
    START_OF_CAREER = 'Начало трудовой деятельности'
    SINGLE_PARENTHOOD = 'Растил ребёнка один (одна)'
    REAL_ESTATE_SALE = 'Продажа недвижимости'
    RETIREMENT = 'Выход на пенсию'
    BUSINESS_FOUNDING = 'Открытие своего бизнеса'
    LONG_TERM_BULLYING_OR_PSYCHOLOGICAL_HARASSMENT = 'Длительное время подвергался травле или психологическим издевательствам'
    ABORTION_FOR_PERSONAL_REASONS = 'Аборт(ы) по личным обстоятельствам'
    CHILD_ADOPTION = 'Усыновление ребёнка/детей'
    MORTGAGE_OR_LARGE_LOAN_REPAYMENT = 'Погашение (частичное или полное) ипотеки/крупного кредита'
    LONG_TERM_ILLNESS = 'Длительное заболевание (продолжающейся более месяца)'
    CHILD_ENROLLMENT_IN_KINDERGARTEN = 'Зачисление ребёнка в детский сад'
    CHILD_UNIVERSITY_ADMISSION_OR_START_OF_PROFESSIONAL_TRAINING = 'Поступление ребёнка в университет/начало профессионального обучения ребёнка'
    CHILD_BIRTH_PLANNING = 'Планирование рождения ребёнка'
    MARRIAGE_REGISTRATION = 'Регистрация брака'
    CHILD_WITH_DISABILITY_CARE = 'Уход за ребёнком with инвалидностью'
    CHILD_WITH_DISABILITY_SOCIAL_INTEGRATION = 'Социализация ребёнка с инвалидностью'
    CLOSE_FAMILY_MEMBER_DEATH = 'Смерть близкого человека'
    CHILD_SCHOOL_ENROLLMENT = 'Поступление ребёнка в школу'
    CHILD_BIRTH = 'Рождение ребёнка'
    PREGNANCY_ANTICIPATION = 'Ожидание рождения ребёнка (беременность)'



class ServiceType(Enum):
    AMENITY = 'Услуга'
    FUNCTION = 'Функция'
    SERVICE = 'Сервис'


class ServiceStatus(Enum):
    IN_QUEUE = 'В очереди на исследование'


class ClientChoice(Enum):
    INTERNAL = 'Внутренний'
    EXTERNAL = 'Внешний'


class DigitalFormatChoice(Enum):
    DIGITAL = 'Цифровой'
    NON_DIGITAL = 'Не цифровой'
