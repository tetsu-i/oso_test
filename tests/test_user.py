from myapp.main import read_all_users, read_user
from oso import Oso
from sqlalchemy.orm import Session


def test_admin_user_can_get_all_users(get_unauth_db: Session, get_oso: Oso):
    # id=1 is admin user(is_admin=True)
    admin_user = read_user(id=1, session=get_unauth_db)
    oso = get_oso
    all_users = read_all_users(actor=admin_user, oso=oso)
    result = list(map(lambda user: user.name, all_users))
    expect = ["admin_user", "orgnaization_A's user 1", "orgnaization_A's user 2", "orgnaization_B's user", "Company_P's User", "Company_P's User2", "Company_Q's User", "Company_R's User"]
    assert result == expect
