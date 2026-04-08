enum UserRole {
    Admin = "Admin",
    User = "User",
    Guest = "Guest"
}
const RoleDescriptions: Record<UserRole, string> = {
    [UserRole.Admin]: "Has full access to all resources.",
    [UserRole.User]: "Can edit content but has limited access to administrative features.",
    [UserRole.Guest]: "Can view content but cannot make any changes."

};

const getRoleDescription = (role: UserRole): string => {
    return RoleDescriptions[role];
}
export {UserRole,   getRoleDescription};