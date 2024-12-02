def unify(expr1, expr2):
    if is_variable_or_constant(expr1) or is_variable_or_constant(expr2):
        if expr1 == expr2:
            return []
        if is_variable(expr1):
            if occurs_check(expr1, expr2):
                return "FAILURE"
            return [(expr2, expr1)]
        if is_variable(expr2):
            if occurs_check(expr2, expr1):
                return "FAILURE"
            return [(expr1, expr2)]
        return "FAILURE"
    if not same_predicate(expr1, expr2):
        return "FAILURE"
    args1 = get_arguments(expr1)
    args2 = get_arguments(expr2)
    if len(args1) != len(args2):
        return "FAILURE"
    SUBST = []
    for i in range(len(args1)):
        s = unify(args1[i], args2[i])
        if s == "FAILURE":
            return "FAILURE"
        if s:
            args1 = apply_substitution(s, args1)
            args2 = apply_substitution(s, args2)
            SUBST.extend(s)
    return SUBST

def is_variable_or_constant(expr):
    return isinstance(expr, str) and expr.islower()

def is_variable(expr):
    return isinstance(expr, str) and expr.islower()

def occurs_check(var, expr):
    if var == expr:
        return True
    if isinstance(expr, list):
        return any(occurs_check(var, sub) for sub in expr)
    return False

def same_predicate(expr1, expr2):
    return expr1[0] == expr2[0] if isinstance(expr1, list) and isinstance(expr2, list) else False

def get_arguments(expr):
    return expr[1:] if isinstance(expr, list) else []

def apply_substitution(subst, expr):
    if isinstance(expr, list):
        return [apply_substitution(subst, sub) for sub in expr]
    for (new, old) in subst:
        if expr == old:
            return new
    return expr

def parse_input(expr):
    try:
        return eval(expr)
    except Exception as e:
        print(f"Error in input format: {e}")
        return None

if __name__ == "__main__":
    print("Unification Program")
    print("Enter expressions in the format: ['predicate', 'arg1', ['sub_predicate', 'arg2']]")
    expr1_input = input("Enter the first expression (Ψ1): ")
    expr1 = parse_input(expr1_input)
    if expr1 is None:
        print("Invalid input for Ψ1. Exiting.")
        exit()
    expr2_input = input("Enter the second expression (Ψ2): ")
    expr2 = parse_input(expr2_input)
    if expr2 is None:
        print("Invalid input for Ψ2. Exiting.")
        exit()
    result = unify(expr1, expr2)
    print("Unification Result:", result)
