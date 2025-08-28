// components/FeaturesSection.tsx

import styles from './MpesaKit.module.css';
interface FeatureItem {
  icon: string;
  title: string;
  description: string;
  features: string[];
}

interface FeaturesSectionProps {
  title: string;
  subtitle: string;
  features: FeatureItem[];
}

export const FeaturesSection: React.FC<FeaturesSectionProps> = ({
  title,
  subtitle,
  features
}) => {
  return (
    <section className={`${styles.features} ${styles.fadeInUp}`} id="features">
      <div className={styles.featuresContainer}>
        <div className={styles.sectionTitle}>
          <h2>{title}</h2>
          <p>{subtitle}</p>
        </div>

        <div className={styles.featuresGrid}>
          {features.map((feature, index) => (
            <FeatureCard key={index} {...feature} />
          ))}
        </div>
      </div>
    </section>
  );
};

const FeatureCard: React.FC<FeatureItem> = ({ icon, title, description, features }) => {
  return (
    <div className={styles.featureCard}>
      <div className={styles.featureIcon}>{icon}</div>
      <h3>{title}</h3>
      <p>{description}</p>
      <ul className={styles.featureList}>
        {features.map((feature, index) => (
          <li key={index}>{feature}</li>
        ))}
      </ul>
    </div>
  );
};
