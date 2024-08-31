def checkMissingValues(schema, newData):
    errors = []
    for key, value in schema.items():
        if value.get('required', False):
            if key not in newData:
                errors.append(f"Missing required key: '{key}'")
            elif newData[key] == "" or newData[key] is None:
                errors.append(f"Empty or undefined value for required key: '{key}'")
    return errors

def checkUniqueness(schema, newData, collection):
    errors = []
    for key, value in schema.items():
        if value.get('unique', False) and key in newData:
            if collection.find_one({key: newData[key]}):
                errors.append(f"The {key} '{newData[key]}' is already in use")
    return errors

def dbSchemaValidator(schema, newData, collection):
    errors = checkMissingValues(schema, newData)
    errors.extend(checkUniqueness(schema, newData, collection))
    if errors:
        raise ValueError(f"Validation errors: {', '.join(errors)}")
    return True