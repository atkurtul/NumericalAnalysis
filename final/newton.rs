#![allow(warnings)]

#[derive(Debug)]
struct poly {
  coeffs: Vec<f64>,
}

impl poly {
  pub fn eval(&self, val: f64) -> f64 {
    self.coeffs.iter().enumerate().fold(0f64, |s, (i,c)| s + val.powf(i as _)*c)
  }

  pub fn base(x0: f64) -> poly {
    poly { coeffs: vec![-x0, 1f64] }
  }
  pub fn mulbase(&self, r: f64)  -> poly{
    self.mul(&poly::base(r))
  }

  pub fn mul(&self, r: &poly) -> poly {
    let mut coeffs = vec![0.;self.coeffs.len()+r.coeffs.len() - 1];
    for (i, c0) in self.coeffs.iter().enumerate() {
      for (j, c1) in r.coeffs.iter().enumerate() {
        coeffs[i+j] += c0*c1;
      }
    }
    poly {
      coeffs
    }
  }

  pub fn mulsca(mut self, sca:f64) -> poly {
    for f in self.coeffs.iter_mut() {
      *f*=sca;
    }
    return self;
  }
}

fn adder(mut long: Vec<f64>, short: Vec<f64>) -> Vec<f64> {
  for (i, s) in short.into_iter().enumerate() {
    long[i] +=s;
  }
  return long;
}

impl std::ops::Add<poly> for poly {
  type Output = poly;
  fn add(self, r: poly) -> poly { 
    
    if self.coeffs.len() > r.coeffs.len() {
      poly { coeffs: adder(self.coeffs, r.coeffs) }
    } else {
      poly { coeffs: adder(r.coeffs, self.coeffs) }
    }
  }
}

impl std::ops::Add<f64> for poly {
  type Output = poly;
  fn add(mut self, r: f64) -> poly { 
    self.coeffs[0] += r;
    return self;
  }
}

impl std::ops::Add<poly> for f64 {
  type Output = poly;
  fn add(self, r: poly) -> poly { 
    r.add(self)
  }
}

impl std::ops::Mul<f64> for poly {
  type Output = poly;
  fn mul(self, sca: f64) -> poly { 
    let mut r = self;
    for f in r.coeffs.iter_mut() {
      *f *= sca;
    }
    return r;
  }
}

impl std::ops::Mul<poly> for f64 {
  type Output = poly;
  fn mul(self, r: poly) -> poly { 
    r.mul(self)
  }
}
#[derive(Debug, Copy, Clone)]
struct point {
  lo: f64,
  hi: f64,
  y: f64
}

impl point {
  pub fn init(lo: (f64, f64), hi: (f64,f64)) -> point {
    point {
      hi: hi.0,
      lo: lo.0,
      y: (hi.1 - lo.1) / (hi.0 - lo.0)
    }
  }

  pub fn next(self, hi: point) -> point {
    point { 
      y: (hi.y - self.y)/(hi.hi - self.lo),
      hi: hi.hi,
      lo: self.lo
    }
  }

}

fn build_tree(init: Vec<(f64,f64)>) -> Vec<f64> {
  let mut coeffs = vec![];
  let mut points = init.iter().zip(init.iter().skip(1)).map(|(lo, hi)| point::init(*lo, *hi)).collect::<Vec<_>>();
  coeffs.push(points[0].y);
  while points.len() > 1 {
    points = points.iter().zip(points.iter().skip(1)).map(|(lo, hi)| lo.next(*hi)).collect::<Vec<_>>();
    coeffs.push(points[0].y);
  }
  coeffs
}

fn main() {

  println!("{:#?}", build_tree(vec![(0.1, 1.2), (0.5, 2.7), (0.7, 3.8), (1.2, 4.7), (1.5, 6.0)]));

  // (0.1, 1.2), (0.5, 2.7), (0.7, 3.8), (1.2, 4.7), (1.5, 6.0) */

  // double xs[N] = {0.1, 0.5, 0.7, 1.2, 1.5};
  // double ys[N] = {1.2, 2.7, 3.8, 4.7, 6.0};

  // 1.2000000000  3.7500000000  2.9166666667  -7.4567099567  11.3636363636

   let poly = 
  1.2000000000  +
  3.7500000000   *  poly::base(0.1) +
  2.9166666667   *  poly::base(0.1).mulbase(0.5) +
  -7.4567099567  *  poly::base(0.1).mulbase(0.5).mulbase(0.7) +
  11.3636363636  *  poly::base(0.1).mulbase(0.5).mulbase(0.7).mulbase(1.2);

  println!("{:?}", poly);
  println!("{:?}", poly.eval(0.1));
  println!("{:?}", poly.eval(0.5));
  println!("{:?}", poly.eval(0.7));
  println!("{:?}", poly.eval(1.2));
  println!("{:?}", poly.eval(1.5));
  // println!("{:?}", poly::base(1.).mulbase(5.).mulbase(7.).mulbase(12.).eval(1.));
  // println!("{:?}", poly::base(1.).mulbase(5.).mulbase(7.).mulbase(12.).eval(5.));
  // println!("{:?}", poly::base(1.).mulbase(5.).mulbase(7.).mulbase(12.).eval(7.));
  // println!("{:?}", poly::base(1.).mulbase(5.).mulbase(7.).mulbase(12.).eval(12.));
}