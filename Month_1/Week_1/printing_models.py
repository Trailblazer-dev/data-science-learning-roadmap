def show_models(unprinted_designs,printed_designs):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while uprinted_designs:
        current_design = uprinted_designs.pop()
        print(f"Printing model: {current_design}")
        printed_designs.append(current_design)
    print("\n--------------------------------")
def show_completed_models(printed_designs):
    """Show all the models that have been printed."""
    print("\nThe following models have been printed:")
    for printed_design in printed_designs:
        print(printed_design)
    
uprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
printed_designs = []
show_models(uprinted_designs[:],printed_designs)
show_completed_models(printed_designs)