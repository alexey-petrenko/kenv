import kenv.constants as consts
import numpy as np

__all__ = ['Beam', 'Particle']


class Particle:
    """
    Creating a particle.
    """

    def __init__(self, *,
                 x: float = .0e0,
                 y: float = .0e0,
                 xp: float = .0e0,
                 yp: float = .0e0,
                 energy: float = .0e0,
                 larmor_angle: float = .0e0):
        """
        Initialization of a particle.

        Parameters
        ----------
        x: float
            Position of the x-axis, [m]
        y: float
            Position of the y-axis, [m]
        xp: float
            Angle of the x-axis, [rad]
        yp: float
            Angle of the y-axis, [rad]
        energy: float
            Energy, [MeV]
        larmor_angle: float
            Larmor angle, [rad]
        """
        self.x = x
        self.y = y
        self.xp = xp
        self.yp = yp
        self.energy = energy
        self.gamma = gamma = self.energy / consts.mass_rest_electron + 1
        self.beta = beta = np.sqrt(1 - 1 / (gamma * gamma))
        self.p = self.momentum = gamma * beta * consts.mass_rest_electron
        self.larmor_angle = larmor_angle

    def __str__(self):
        return 'Particle parameters:' + '\n' \
            + '\tHorizontal position\t%0.1f mm' % (self.x * 1e3) + '\n' \
            + '\tVertical position\t%0.1f mm' % (self.y * 1e3) + '\n' \
            + '\tHorizontal angle\t%0.1f mrad' % (self.xp * 1e3) + '\n' \
            + '\tVertical angle\t%0.1f mrad' % (self.yp * 1e3) + '\n' \
            + '\tEnergy\t%0.3f MeV' % (self.energy) + '\n'


class Beam:
    """
    Creating an electron beam.
    """

    def __init__(self, *,
                 current: float = .0e0,
                 energy: float = .0e0,
                 radius: float = .0e0,
                 radius_x: float = .0e0,
                 radius_y: float = .0e0,
                 rp: float = .0e0,
                 radius_xp: float = .0e0,
                 radius_yp: float = .0e0,
                 normalized_emittance: float = .0e0,
                 normalized_emittance_x: float = .0e0,
                 normalized_emittance_y: float = .0e0,
                 x: float = .0e0,
                 y: float = .0e0,
                 xp: float = .0e0,
                 yp: float = .0e0,
                 larmor_angle: float = .0e0,
                 charge: int = -1):
        """
        Initialization of an electron beam.

        Parameters
        ----------
        current: float
            Beam current, [A]
        energy: float
            Beam energy, [MeV]
        radius: float
            Beam radius, [m]
        radius_x: float, optional
            Elliptical beam radius along the x-axis, [m]
        radius_y: float, optional
            Elliptical beam radius along the y-axis, [m]
        rp: float
            Beam radius prime, [rad]
        radius_xp: float, optional
            Elliptical beam radius prime along the x-axis, [rad]
        radius_yp: float, optional
            Elliptical beam radius prime along the y-axis, [rad]
        normalized_emittance: float
            Beam normalized emittance, [m*rad]
        normalized_emittance_x: float, optional
            Elliptical beam normalized emittance along the x-axis, [m*rad]
        normalized_emittance_y: float, optional
            Elliptical beam normalized emittance along the y-axis, [m*rad]

        x: float, optional
            Offset of the centroid along the x-axis, [m]
        xp: float, optional
            Centroid rotation in the z-x plane, [rad]
        y: float, optional
            Offset of the centroid along the y-axis, [m]
        yp: float, optional
            Centroid rotation in the z-y plane, [rad]
        larmor_angle: float, optional
            Centroid larmor angle, [rad]
        charge: int, optional
            Particle charge (dev!)
        """
        self.current = current
        self.energy = energy
        self.radius = radius
        self.rp = rp
        self.radius_x = radius_x
        self.radius_y = radius_y
        self.radius_xp = radius_xp
        self.radius_yp = radius_yp
        self.normalized_emittance = normalized_emittance
        self.normalized_emittance_x = normalized_emittance_x
        self.normalized_emittance_y = normalized_emittance_y
        if radius != .0e0:
            self.radius_x = radius
            self.radius_y = radius
        if rp != .0e0:
            self.radius_xp = rp
            self.radius_yp = rp
        if normalized_emittance != .0e0:
            self.normalized_emittance_x = normalized_emittance
            self.normalized_emittance_y = normalized_emittance

        self.x = x
        self.y = y
        self.xp = xp
        self.yp = yp
        self.larmor_angle = larmor_angle

        self.charge = charge

        self.gamma = gamma = self.energy / consts.mass_rest_electron + 1
        self.beta = beta = np.sqrt(1 - 1 / (gamma * gamma))

        self.p = self.momentum = gamma * beta * consts.mass_rest_electron
        self.px = self.p * self.radius_xp
        self.py = self.p * self.radius_yp
        self.pz = self.p
        self.description = ''

    def __str__(self):
        self.description = 'Beam parameters:\n' \
            + f'\tCurrent\t{self.current} A\n' \
            + f'\tEnergy\t{self.energy} MeV\n' \
            + f'\tTotal momentum\t{self.momentum} MeV/c\n' \
            + f'\tRel. factor\t{self.gamma}\n' \
            + f'\tRadius x\t{self.radius_x * 1e3} mm\n' \
            + f'\tRadius y\t{self.radius_y * 1e3} mm\n' \
            + f'\tRadius x prime\t{self.radius_xp * 1e3} mrad\n' \
            + f'\tRadius y prime\t{self.radius_yp * 1e3} mrad\n' \
            + f'\tHorizontal centroid position\t{self.x * 1e3} mm\n' \
            + f'\tVertical centroid position\t{self.y * 1e3} mm\n' \
            + f'\tHorizontal centroid angle\t{self.xp * 1e3} mrad\n' \
            + f'\tVertical centroid angle\t{self.yp * 1e3} mrad\n' \
            + f'\tLarmor angle\t{self.larmor_angle} rad\n' \
            + f'\tNorm. emitt x\t{self.normalized_emittance_x*1e6} mm*mrad\n'
        return self.description
