# Enrolment System

Description: ...

## Post Condition

Python version >= 3.11

- `StrEnum` need Python versions 3.11

## Run Application

This application separates in 2 modes: CLI and GUI. We can use `--mode <cli|gui>` or `-m <cli|mode>` to switch between two mode.

By default, the system will start with GUI mode

For CLI mode:

```
python3 main.py -m cli
```

## File Structure

```
├── data
│ ├── enrolment_system.data
├── src
│ ├── base (abstract class)
│ ├── entities (entity abstract class)
│ ├── core (utils, constants)
│ └── entities
│ └── enums
├── tests (optional)
├── main.py
├── setup.py
├── README.md
```
