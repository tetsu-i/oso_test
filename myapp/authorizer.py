from typing import Callable

from oso import Oso, Relation
from polar.data.adapter.sqlalchemy_adapter import SqlAlchemyAdapter
from sqlalchemy.orm import Session

from myapp.models.company import Company
from myapp.models.organization import Organization
from myapp.models.user import User
from myapp.models.users_company import UsersCompany
from myapp.models.users_organization import UsersOrganization


def build_oso() -> Callable[[Session], Oso]:
    _oso = Oso()
    _oso.register_class(
        User,
        fields={
            "id": int,
            "name": str,
            "is_admin": bool,
            "users_organizations": Relation(
                kind="many",
                other_type="UsersOrganization",
                my_field="id",
                other_field="user_id",
            ),
            "users_companies": Relation(
                kind="many",
                other_type="UsersCompany",
                my_field="id",
                other_field="user_id",
            ),
        },
    )
    _oso.register_class(
        Organization,
        fields={
            "id": int,
            "name": str,
            "users_organizations": Relation(
                kind="many",
                other_type="UsersOrganization",
                my_field="id",
                other_field="organization_id",
            ),
            "companies": Relation(
                kind="many",
                other_type="Company",
                my_field="id",
                other_field="organization_id",
            ),
        },
    )
    _oso.register_class(
        UsersOrganization,
        fields={
            "id": int,
            "user_id": int,
            "organization_id": int,
            "admin": Relation(
                kind="one",
                other_type="User",
                my_field="user_id",
                other_field="id",
            ),
            "organization": Relation(
                kind="one",
                other_type="Organization",
                my_field="organization_id",
                other_field="id",
            ),
        },
    )
    _oso.register_class(
        Company,
        fields={
            "id": int,
            "organization_id": int,
            "users_companies": Relation(
                kind="many",
                other_type="UsersCompany",
                my_field="id",
                other_field="company_id",
            ),
            "organization": Relation(
                kind="one",
                other_type="Organization",
                my_field="organization_id",
                other_field="id",
            ),
        },
    )
    _oso.register_class(
        UsersCompany,
        fields={
            "id": int,
            "user_id": int,
            "company_id": int,
            "user": Relation(
                kind="one",
                other_type="User",
                my_field="user_id",
                other_field="id",
            ),
            "company": Relation(
                kind="one",
                other_type="Company",
                my_field="company_id",
                other_field="id",
            ),
        },
    )
    _oso.load_files(["myapp/main.polar"])

    def set_filter(session: Session) -> Oso:
        _oso.set_data_filtering_adapter(SqlAlchemyAdapter(session))
        return _oso

    return lambda session: set_filter(session=session)
