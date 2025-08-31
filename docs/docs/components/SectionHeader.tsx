import React from 'react';
import styles from './SectionHeader.module.css';

type Size = 'large' | 'small';

interface SectionHeaderProps {
  title: React.ReactNode;
  subtitle?: React.ReactNode;
  gradient?: boolean;
  size?: Size;
  className?: string;
}

const SectionHeader: React.FC<SectionHeaderProps> = ({
  title,
  subtitle,
  gradient = false,
  size = 'large',
  className = ''
}) => {
  const headerClass = size === 'large' ? styles.pageTitle : styles.sectionTitle;
  const titleClass = gradient ? `${headerClass} ${styles.gradient}` : headerClass;

  return (
    <div className={`${styles.headerContainer} ${className}`}>
      <h1 className={titleClass}>{title}</h1>
      {subtitle && (
        <p className={size === 'large' ? styles.pageSubtitle : styles.sectionSubtitle}>
          {subtitle}
        </p>
      )}
    </div>
  );
};

export default SectionHeader;
