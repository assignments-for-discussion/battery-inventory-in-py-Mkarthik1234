
def count_batteries_by_health(present_capacities):
  healthy = 0
  exchange = 0
  failed = 0
  for i in present_capacities:
      SoH = 100 * i // 120
      if SoH >= 80:
        healthy+=1
      elif SoH < 80 and SoH >= 62:
        exchange+=1
      else:
        failed+=1
  
  return {
    "healthy": healthy,
    "exchange": exchange,
    "failed": failed
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
