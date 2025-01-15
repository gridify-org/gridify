from hypothesis import strategies as st

from gridify.typings import IDType


@st.composite
def uuid_strategy(draw: st.DrawFn) -> IDType:
    return draw(st.uuids())
