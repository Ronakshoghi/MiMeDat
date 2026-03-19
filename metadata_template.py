"""
The JSON template with all the mandatory and optional elements for the metadata schema:"https://github.com/Ronakshoghi/MetadataSchema/blob/main/microstructure_sensitive_mechanical_metadata_schema.json".
Once created, the data object can be validated against the JSON schema using any online JSON validator for example :https://www.jsonschemavalidator.net/. The script generate a unique identifier based on the all mandatory fields and
saves the JSON file with the identifier as the filename.The identifier will be included in the json file as well. The script also removes all the empty entries from the JSON object before saving it.

Author: Ronak Shoghi
ICAMS, Ruhr University Bochum, Germany
August 2024
"""
import json
import hashlib

def remove_empty_entries(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            cleaned_value = remove_empty_entries(value)
            if cleaned_value is not None and cleaned_value != {} and cleaned_value != []:
                new_dict[key] = cleaned_value
        return new_dict if new_dict else None
    elif isinstance(data, list):
        cleaned_list = filter(None, (remove_empty_entries(item) for item in data))
        return [item for item in cleaned_list if item != {} and item != []]
    else:
        return data if data is not None else None

def create_hash(data, mandatory_fields):
    hash_string = ""
    for field in mandatory_fields:
        value=data.get(field)
        if value is not None:
            hash_string += json.dumps(value, sort_keys = True)
    hash_object = hashlib.md5(hash_string.encode())
    hash = hash_object.hexdigest()[:8]
    return hash

Dict_Test = {
    "$schema": "https://github.com/Ronakshoghi/MiMeDat/blob/main/microstructure_sensitive_mechanical_metadata_schema.json",
    "identifier": "None",
    "title": None,
    "creator": [None],
    "creator_ORCID": [None],
    "creator_affiliation": [None],
    "creator_institute": [None],
    "creator_group": [None],
    "contributor": [None],
    "contributor_ORCID": [None],
    "contributor_affiliation": [None],
    "contributor_institute": [None],
    "contributor_group": [None],
    "date": None,
    "shared_with": [
      {
        "access_type": None,
        "access_list": [None]
      }
    ],
    "description": None,
    "rights": None,
    "rights_holder": [None],
    "funder_name": None,
    "fund_identifier": None,
    "publisher": None,
    "relation": [None],
    "user_extra_information": None,
    "keywords": [None],
    "software": None,
    "software_version": None,
    "system": None,
    "system_version": None,
    "CPU_specifications": None,
    "input_path": None,
    "results_path": None,
    "system_extra_information": None,
    "RVE_size": [None, None, None],
    "RVE_continuity": True,
    "discretization_type": None,
    "discretization_unit_size": [None, None, None],
    "discretization_count": None,
    "origin": {
        "software": None,
        "software_version": None,
        "system": None,
        "system_version": None,
        "input_path": None,
        "results_path": None
        },
    "global_temperature": None,
    "mechanical_BC": [
        {"vertex_list": [None],
         "constraints": [None, None, None],
         "loading_type": None,
         "loading_mode": None,
         "applied_load": [{"magnitude": None,
                           "frequency": None,
                           "duration": None,
                           "R": None}]
         }
    ],
    "thermal_BC": [
        {"vertices_list": [None],
        "constraints": [None, None, None],
        "loading_mode": None,
        "applied_load": [{"magnitude": None,
                           "frequency": None,
                           "duration": None}]
        }
    ],
    "phase": [{
        "phase_name": None,
        "phase_id": None,
        "volume_fraction": None,
        "lattice_structure": None,
        "constitutive_model": {
            "schema": None,
            "elastic_model_name": None,
            "elastic_parameters": None,
            "plastic_model_name": None,
            "plastic_parameters": {None},
            "damage_model_name": None,
            "damage_parameters": {None},
            "units": {None}
        },
        "orientation": {
            "euler_angles": {None},
            "grain_count": None,
            "orientation_identifier": None,
            "texture_type": None,
            "software": None,
            "software_version": None
        }}
    ],
    "stress": {},
    "total_strain": {},
    "plastic_strain": {},
    "units": {}
}
mandatory_fields = [
    "title",
    "creator",
    "creator_affiliation",
    "date",
    "shared_with",
    "rights",
    "rights_holder",
    "software",
    "software_version",
    "system",
    "system_version",
    "processor_specifications",
    "input_path",
    "results_path",
    "RVE_size",
    "RVE_continuity",
    "discretization_type",
    "discretization_unit_size",
    "discretization_count",
    "mechanical_BC",
    "phase",
    "stress",
    "total_strain",
    "units"
  ]
cleaned_dict = remove_empty_entries(Dict_Test)

if cleaned_dict:
    short_hash_filename = create_hash(cleaned_dict, mandatory_fields)
    cleaned_dict["identifier"] = short_hash_filename
    with open(f'{short_hash_filename}.json', 'w') as fp:
        json.dump(cleaned_dict, fp, indent=4)
    print(f"JSON saved successfully with filename: {short_hash_filename}.json")
else:
    print("No relevant data to save.")