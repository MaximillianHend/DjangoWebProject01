from .taxonomy import TAXONOMY
from .descriptor_templates import DESCRIPTOR_TEMPLATES
from .skill_map import SKILL_MAP

OUTCOME_CRITERIA_MAP = {
    'DS11-1': [
        'Communication',
        'Project progression',
        'Testing methodology',
        'Project Solution',
        'Understanding of the system',
        'Optimisations of the system',

    ],


    'DS11-2': [
        'Communication',
        'Project progression',
        'Testing methodology',
        'Project Solution',
        'Understanding of the system',
        'Optimisations of the system',

    ],


    'DS12-3': [
        'Communication',
        'Project progression',
        'Testing methodology',
        'Project Solution',
        'Understanding of the system',
        'Optimisations of the system',

    ]
}


def generate_rubric(selected_outcomes):
    criteria = []

    for outcome in selected_outcomes:

        if outcome in OUTCOME_CRITERIA_MAP:
            criteria.extend(OUTCOME_CRITERIA_MAP[outcome])

    criteria = list(set(criteria))
    rubric = {}

    for criterion in criteria:
        rubric[criterion] = {}
        template = DESCRIPTOR_TEMPLATES[criterion]
        skill = SKILL_MAP[criterion]

        for band, quality in TAXONOMY.items():
            descriptor = template.format(quality=quality,skill=skill)
            rubric[criterion][band] = descriptor

    return rubric