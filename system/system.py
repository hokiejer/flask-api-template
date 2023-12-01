import os

class EnvironmentError(Exception):
    """Base class for environment related exceptions."""
    pass

class VariableNotDefinedError(EnvironmentError):
    """Exception for when an environment variable isn't defined."""
    pass

class LabelNotDefinedError(EnvironmentError):
    """Exception for when a label doesn't match any system variable."""
    pass

class ExistingDeclarationError(EnvironmentError):
    """Exception for when a variable declaration already exists."""
    pass

class System:
    _env_vars = {}
    _defaults = {}
    _overrides = {}

    @classmethod
    def declare(cls, label, env_var, default=None):
        """Declare an environmental variable."""
        if label in cls._env_vars:
            raise ExistingDeclarationError(f"The label {label} already has a declaration.")
        cls._env_vars[label] = env_var
        if default is not None:
            cls._defaults[label] = default

    @classmethod
    def undeclare(cls, label):
        """Remove an environmental variable from mappings."""
        cls._env_vars.pop(label, None)
        cls._defaults.pop(label, None)

    @classmethod
    def read_environment_variable(cls, label):
        """Read a variable from the environment."""
        varname = cls._env_vars.get(label)
        if varname is not None:
            return os.getenv(varname)
        raise LabelNotDefinedError(f"The label {label} is not defined.")

    @classmethod
    def defined(cls, label):
        """Check if a variable is set, has a default, or has an override."""
        if label in cls._overrides:
            return True
        if cls.read_environment_variable(label) is not None:
            return True
        if label in cls._defaults:
            return True
        return False

    @classmethod
    def getvar(cls, label):
        """Read a variable and return it, or its default if not set."""
        value = cls._overrides.get(label) or cls.read_environment_variable(label) or cls._defaults.get(label)
        if value is None:
            raise VariableNotDefinedError(f"The environment variable for {label} is not defined and has no default.")
        return value

    @classmethod
    def setvar(cls, label, new_value):
        """Set the override value for a variable."""
        cls._overrides[label] = new_value

    @classmethod
    def unsetvar(cls, label):
        """Clear the override value for a variable."""
        cls._overrides.pop(label, None)

    @classmethod
    def getpath(cls, varname):
        """Read an environment path variable and return as a list."""
        pathdata = cls.getvar(varname)
        if pathdata is None:
            raise EnvironmentError(f"Environment variable {varname} needs to be defined.")
        return pathdata.split(':')

    # ... Additional methods like suite_path, tpl_path, tp_path, etc., can be defined similarly ...

