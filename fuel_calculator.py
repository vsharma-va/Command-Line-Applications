import argparse


def calculate_fuel(fuel_per_lap, total_race_time, average_lap_min, average_lap_seconds, average_lap_tenths):
    seconds_to_min = average_lap_seconds / 60
    tenths_to_min = average_lap_tenths / (60 * 60)
    total_average_lap = average_lap_min + seconds_to_min + tenths_to_min
    total_num_laps = total_race_time / total_average_lap
    total_fuel_required = total_num_laps * fuel_per_lap
    return total_fuel_required


def main():
    parser = argparse.ArgumentParser()
    event = parser.add_mutually_exclusive_group()
    parser.add_argument('fpl', type=float, help='Fuel Per Lap')
    parser.add_argument('trt', type=float, help='Total Race Time')
    parser.add_argument('avlm', type=int, help='Minute part of the lap time')
    parser.add_argument('avls', type=int, help='Seconds part of the lap time')
    parser.add_argument('avlt', type=int, help='Tenths part of the lap time')
    parser.add_argument('track', type=str, help='Track Name', nargs='?')
    parser.add_argument('-s', '--save', help='Save Details in a text file', action='store_true')
    event.add_argument('-d', '--detailed', help='Detailed Output', action='store_true')
    event.add_argument('-q', '--quiet', help='Concise Output', action='store_true')
    args = parser.parse_args()
    if args.detailed:
        print(f'''Fuel Per Lap = {args.fpl} \nTotal Race Time = {args.trt}
Average Lap Time = {args.avlm}:{args.avls}.{args.avlt}''')
        print(calculate_fuel(args.fpl, args.trt, args.avlm, args.avls, args.avlt))
    elif args.quiet:
        print(calculate_fuel(args.fpl, args.trt, args.avlm, args.avls, args.avlt))

    if args.save and args.track:
        file = open('F://IDEs//Python Saves//CLI//acc.txt', 'a')
        file.write('\n')
        file.writelines(f'''\nFuel Per Lap = {args.fpl} \nTotal Race Time = {args.trt}
Average Lap Time = {args.avlm}:{args.avls}.{args.avlt} \nTrack Name = {args.track}''')
        file.close()
    elif args.save and not args.track:
        print("If you want to save you will have to provide track name")


if __name__ == '__main__':
    main()
    print()
