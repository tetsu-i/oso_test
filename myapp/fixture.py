from sqlalchemy.orm import Session

from myapp.database import UnauthSession
from myapp.models.company import Company
from myapp.models.organization import Organization
from myapp.models.user import User


def main():
    session: Session = UnauthSession()
    admin_user = User(
        name="admin_user",
        is_admin=True,
    )
    admin_org = Organization(name="Admin_ORG")
    admin_user.organizations = [admin_org]

    orgnaization_a = Organization(name="orgnaization A")
    orgnaization_b = Organization(name="orgnaization B")

    user_oa_1 = User(
        name="orgnaization_A's user 1",
        is_admin=False,
    )
    user_oa_2 = User(
        name="orgnaization_A's user 2",
        is_admin=False,
    )
    user_ob = User(
        name="orgnaization_B's user",
        is_admin=False,
    )

    orgnaization_a.users = [user_oa_1, user_oa_2]
    orgnaization_b.users = [user_ob]

    session.add_all(
        [
            admin_user,
            admin_org,
            orgnaization_a,
            orgnaization_b,
            user_oa_1,
            user_oa_2,
            user_ob,
        ]
    )
    session.flush()

    admin_company = Company(name="Admin Com", organization_id=admin_org.id)
    admin_user.companies = [admin_company]

    company_p = Company(name="Company P", organization_id=orgnaization_a.id)
    company_q = Company(name="Company Q", organization_id=orgnaization_a.id)
    company_r = Company(name="Company R", organization_id=orgnaization_b.id)

    admin_cp_1 = User(
        name="Company_P's User",
        is_admin=False,
    )
    admin_cp_2 = User(
        name="Company_P's User2",
        is_admin=False,
    )
    admin_cq_1 = User(
        name="Company_Q's User",
        is_admin=False,
    )
    admin_cr_1 = User(
        name="Company_R's User",
        is_admin=False,
    )

    company_p.users = [admin_cp_1, admin_cp_2]
    company_q.users = [admin_cq_1]
    company_r.users = [admin_cr_1]

    session.add_all(
        [
            admin_company,
            company_p,
            company_q,
            company_r,
            admin_cp_1,
            admin_cp_2,
            admin_cq_1,
            admin_cr_1,
        ]
    )
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
