def convert_errors_to_sentence(marshmallow_errors):
    errors = ''
    for k, v in marshmallow_errors.items():
        errors += str(k)
        errors += ': '
        for error in v:
            errors += str(error)
            errors += ' '
    return errors