from kernel.models.auth import User
from kernel.models.generics import (
    ContactInformation,
    LocationInformation,
)
from kernel.models.institute import (
    # Abstract models for customised implementations
    AbstractDepartment,
    AbstractCentre,
    AbstractBranch,

    # Concrete models for default implementation
    Department,
    Centre,
    Branch
)
from kernel.models.person import (
    # Abstract models for customised implementations
    AbstractPerson,

    # Concrete models for default implementation
    Person,
)
from kernel.models.personal_information import (
    # Abstract models for customised implementations
    AbstractBiologicalInformation,
    AbstractPoliticalInformation,
    AbstractFinancialInformation,

    # Concrete models for default implementation
    BiologicalInformation,
    FinancialInformation,
    PoliticalInformation,
)
from kernel.models.roles import (
    # Abstract models for customised implementations
    AbstractStudent,

    # Concrete models for default implementation
    Student,
)
