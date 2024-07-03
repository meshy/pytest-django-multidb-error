import pytest
from django.db.transaction import atomic


@pytest.mark.django_db(databases=["default"])
def test_wrong_db():
    with pytest.raises(RuntimeError, match="Database access not allowed"):
        with atomic(using="secondary"):
            pass
