from rpw import uidoc, doc, DB
from rpw import List


def to_element_ids(elements):
    """ Coerces list of elements into element ids.
    Args:
        elements ([``DB.Element``]) = Iterable list or single ``DB.Element``

    Returns:
        []``DB.ElementId``]: List of Element Ids.
    """
    if not isinstance(elements, list):
        elements = [elements]

    element_ids = []
    for element in elements:
        if isinstance(element, DB.Element):
            element_ids.append(element.Id)
        elif (isinstance(element, DB.ElementId) or
              isinstance(element, DB.ElementId.InvalidElementId)):
            element_ids.append(element)

    return element_ids


def to_elements(element_references):
    """ Coerces element reference (``int``, or ``ElementId``) into ``DB.Element``.
    Remains unchanged if it's already ``DB.Element``. Accepts single object or lists

    Args:
        element_references ([``DB.ElementId``, ``int``, ``DB.Element``]): Element Reference, single or list

    Returns:
        [``DB.Element``]: Elements
    """
    if not isinstance(element_references, list):
        element_references = [element_references]

    elements = []

    for element_reference in element_references:

        if isinstance(element_reference, DB.ElementId):
            element = doc.GetElement(element_reference)

        elif isinstance(element_reference, int):
            element = doc.GetElement(DB.ElementId(element_reference))

        elif isinstance(element_reference, DB.Element):
            element = element_reference

        else:
            raise RPW_TypeError('Element, ElementId, or int', type(element_reference))

        elements.append(element)

    return elements
