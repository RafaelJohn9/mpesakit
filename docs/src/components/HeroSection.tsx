// components/HeroSection.tsx
import React from 'react';
import styles from './MpesaKit.module.css';
import { CodeDemo } from './CodeDemo';

interface HeroSectionProps {
  title: string;
  description: string;
  badges: string[];
  primaryCTA: {
    text: string;
    href: string;
  };
  secondaryCTA: {
    text: string;
    href: string;
  };
}

export const HeroSection: React.FC<HeroSectionProps> = ({
  title,
  description,
  badges,
  primaryCTA,
  secondaryCTA
}) => {
  return (
    <section className={styles.hero}>
      <div className={styles.heroContainer}>
        <div className={styles.heroContent}>
          <h1>{title}</h1>
          <p>{description}</p>

          <div className={styles.heroBadges}>
            {badges.map((badge, index) => (
              <span key={index} className={styles.badge}>{badge}</span>
            ))}
          </div>

          <div className={styles.ctaButtons}>
            <a href={primaryCTA.href} className={`${styles.btn} ${styles.btnPrimary}`}>
              {primaryCTA.text}
            </a>
            <a href={secondaryCTA.href} className={`${styles.btn} ${styles.btnSecondary}`}>
              {secondaryCTA.text}
            </a>
          </div>
        </div>

        <CodeDemo />
      </div>
    </section>
  );
};