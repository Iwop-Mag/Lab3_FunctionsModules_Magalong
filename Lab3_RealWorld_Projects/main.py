"""Run the Exercise 3 telemetry monitoring report."""

from functs import process_telemetry, telemetry_stream


LAST_NAME = 'Magalong'
STUDENT_ID = 'TUPM-26-1134'
SEED_NUM = int(STUDENT_ID[-1])
FAVORITE_ARTIST = 'The Weeknd'


def main():
    """Generate and print the final diagnostic report."""
    print('Student:', LAST_NAME)
    print('Seed Number:', SEED_NUM)
    print('Favorite Artist:', FAVORITE_ARTIST)
    print('Telemetry stream ready: generator created')

    transformed = map(
        lambda value: value if not isinstance(value, (int, float)) else value + SEED_NUM,
        telemetry_stream(LAST_NAME, FAVORITE_ARTIST, SEED_NUM),
    )
    report = process_telemetry(transformed)

    print(f'\n\n=== EXERCISE 3: TELEMETRY MONITORING ===')
    print(f'Student: {LAST_NAME} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}')
    print(f"Processed readings: {report['processed']}")
    print(f"Valid readings: {report['valid']}")
    print(f"Invalid readings: {report['invalid']}")
    print(f"Detected abnormal conditions: {report['abnormal']}")
    print(f"Overall equipment status: {report['status']}")
    print(f'Major processing calls monitored: {process_telemetry.calls}')
    for index, trace in enumerate(report['traces'], start=1):
        print(f'Abnormal trace {index}:')
        print('\n'.join(f'  {step}' for step in trace))


if __name__ == '__main__':
    main()
