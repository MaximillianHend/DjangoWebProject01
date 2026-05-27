from .taxonomy import TAXONOMY
from .descriptor_templates import DESCRIPTOR_TEMPLATES
from .skill_map import SKILL_MAP

OUTCOME_CRITERIA_MAP = {
    "EN11-1": [
        "Analysis",
        "Evidence",
        "Evaluation"
    ],

    "EN11-3": [
        "Structure",
        "Communication",
        "Argument"
    ]
}

def get_criteria_from_outcomes(selected_outcomes):

    criteria = []

    for outcome in selected_outcomes:

        if outcome in OUTCOME_CRITERIA_MAP:
            criteria.extend(
                OUTCOME_CRITERIA_MAP[outcome]
                )

        return list(set(criteria))



def generate_descriptors(criteria):

    rubric = {}

    for criterion in criteria:

        rubric[criterion] = {}

        bands = TAXONOMY[criterion]

        template = DESCRIPTOR_TEMPLATES[criterion]

        skill = SKILL_MAP[criterion]

        for band, quality in bands.items():

            descriptor = template.format(
                quality=quality,
                skill=skill
            )

            rubric[criterion][band] = descriptor

    return rubric