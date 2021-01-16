

def simpson(a, b, f):
  return ((b-a)/6.0) * (f(a) + 4.0* f((a+b)*0.5) + f(b))


def seg_simpson(lo, hi, f, segments):
  s = 0.0
  step = (hi-lo)/segments
  for _ in range(segments):
    s += simpson(lo, lo := lo + step, f)
  return s


print("Simpson's approximations with n segments where:")
print("\tn = 1 => ∫¹x² ≈", seg_simpson(0, 1, lambda x: x*x, 1))
print("\tn = 2 => ∫¹x² ≈", seg_simpson(0, 1, lambda x: x*x, 2))
print("\tn = 4 => ∫¹x² ≈", seg_simpson(0, 1, lambda x: x*x, 4))
print("\tn = 6 => ∫¹x² ≈", seg_simpson(0, 1, lambda x: x*x, 6))

