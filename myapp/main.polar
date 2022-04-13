actor User {
    permissions = ["read"];
}

has_permission(user: User, "read", user: User);
has_permission(user: User, "read", _: User) if
    user.is_admin;

has_permission(user: User, "read", other: User) if
    uo in user.users_organizations and
    other_uo in other.users_organizations and
    uo.organization_id = other_uo.organization_id;

has_permission(user: User, "read", other: User) if
    uc in user.users_companies and
    other_uc in other.users_companies and
    uc.company_id = other_uc.company_id;

allow(actor, action, resource) if
    has_permission(actor, action, resource);