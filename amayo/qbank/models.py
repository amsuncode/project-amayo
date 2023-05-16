from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User


class Tag(models.Model):
    """Handler for tags attribute for questions.

    Has a a many-to-many relationship with `Qbank.tag` attribute
    """

    tag = models.CharField(max_length=50)
    """Tags about key themes related to the question.

    Mainly helps with querying the database
    """


class Qbank(models.Model):
    """This class represents a question object.

    Attributes of the question object include:
        * The question stem
        * The question type eg. MCQ, SAQ etc
        * Appropriate responses for the question type eg marking points,
                        choices
        * Year of study the question applies to
        * The subunit for the year of study
        * Tags to help in searching for questions
        * Metadata information - `created_at`, `last_updated`, `user` who added
                    the question
    All these attributes correspond to table columns in the database.
    """

    QUESTION_TYPES = (
        ('SAQ', 'Short Answer Questions (SAQs)'),
        ('MCQ', 'Multiple Choice Questions (MCQs)'),
        ('ESSAY', 'Essays'),
        ('VIVA', 'Vivas (Orals)'),
        ('OSCE', 'OSCEs')
    )
    """A tuple of the types of questions available.

    Used to create a drop-down list in the forms.
    Values on the right represent what appears on the form for use to select,
    while those on the left are the values captured and sent to the
    backend for processing.
    """

    YEARS_OF_STUDY = (
        (1, 'First year (I)'),
        (2, 'Second year (II)'),
        (3, 'Third year (III)'),
        (4, 'Fourth year (IV)'),
        (5, 'Fifth year (V)'),
        (6, 'Sixth year (VI)'),
    )
    """A tuple of the years of study in medical school.

    Used to create a drop-down list in the forms.
    Values on the right represent what appears on the form for use to select,
    while those on the left are the values captured and sent to the
    backend for processing.
    """

    # FIXME - Fully populate this list, and add correct course codes as the
    #               value
    UNITS = (
        (1, 'Anatomy'),
        (2, 'Biochemistry'),
        (3, 'Pathology'),
        (4, 'Internal Medicine'),
        (5, 'Psychiatry'),
        (6, 'Pharmacology'),
    )
    """A tuple of the units in medical school.

    Used to create a drop-down list in the forms.
    Values on the right represent what appears on the form for use to select,
    while those on the left are the values captured and sent to the
    backend for processing.
    """

    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES)
    """The format of the question.

    See `QUESTION_TYPES` for the full list.
    """

    year_of_study = models.IntegerField(choices=YEARS_OF_STUDY)
    """The year of medical school this question applies to.

    Will capture a value between `[1 - 6]` inclusive.
    """

    # TODO - Change to `models.CharField` when course codes are added
    unit = models.IntegerField(choices=UNITS)
    """The unit of medical school that the question originates from"""

    question_text = models.TextField()
    """The question stem"""

    question_response = JSONField()
    """The appropriate responses relevant to the specific question type.

    Is handled as a python `dict` in code and stored as a JSON in database.
    This allows storing of responses appropriate for the `quesiton_type`.
    See below:
        * `MCQs` - will store options to choose from, the correct option and
                the explanations for each option
        * `SAQs`, `Essay`, `Viva`, `OSCE` - will store marking points
    """

    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    """The user who added the question.

    Is usually an `admin` user.
    """

    # TODO - Implement tags correctly so that user can enter as a
    #               comma separated list of text
    tag = models.ManyToManyField(Tag)
    """Tags about key themes related to the question.

    Mainly helps with querying the database
    """

    # TODO - Implement storage for Images here

    # TODO - Implement storage for other file types here
    #           - includes: video, audioclips

    created_at = models.DateTimeField(auto_created=True)
    """Date and time when question was added"""

    last_updated = models.DateTimeField(auto_now=True)
    """Date and time when quesiton was last updated"""