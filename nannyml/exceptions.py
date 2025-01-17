# Author:   Niels Nuyttens  <niels@nannyml.com>
#
# License: Apache Software License 2.0

"""Custom exceptions."""


class InvalidArgumentsException(BaseException):
    """An exception indicating that the inputs for a function are invalid."""


class ChunkerException(BaseException):
    """An exception indicating an error occurred somewhere during chunking."""


class MissingMetadataException(BaseException):
    """An exception indicating metadata columns are missing from the dataframe being processed."""


class InvalidReferenceDataException(BaseException):
    """An exception indicating the reference data provided are invalid."""


class CalculatorException(BaseException):
    """An exception indicating an error occurred during (drift) calculation."""


class CalculatorNotFittedException(CalculatorException):
    """An exception indicating a calculator was not fitted before using it in calculations."""


class NotFittedException(BaseException):
    """An exception indicating an object was not fitted before using it."""


class WriterException(BaseException):
    """An exception indicating something went wrong whilst trying to write out results."""


class ReaderException(BaseException):
    """An exception indicating something went wrong whilst trying to read out data."""


class IOException(BaseException):
    """An exception indicating something went wrong during IO."""
