import React from 'react';
import styles from './Alert.module.css';

type AlertType = 'info' | 'warning' | 'error' | 'success';

interface AlertProps {
  type?: AlertType;
  title?: React.ReactNode;
  children?: React.ReactNode;
  icon?: React.ReactNode;
  className?: string;
}

const Alert: React.FC<AlertProps> = ({
  type = 'info',
  title,
  children,
  icon,
  className = ''
}) => {
  const getDefaultIcon = (t: AlertType): React.ReactNode => {
    const icons: Record<AlertType, React.ReactNode> = {
      warning: '⚠️',
      error: '❌',
      success: '✅',
      info: '💡'
    };
    return icons[t] ?? '💡';
  };

  const displayIcon = icon ?? getDefaultIcon(type);
  const variant = `alert${type.charAt(0).toUpperCase()}${type.slice(1)}`;

  return (
    <div className={`${styles.alert} ${styles[variant]} ${className}`} role="alert">
      <div className={styles.alertContent}>
        {title && (
          <div className={styles.alertTitle}>
            <span className={styles.alertIcon}>{displayIcon}</span>
            <strong>{title}</strong>
          </div>
        )}
        <div className={styles.alertBody}>{children}</div>
      </div>
    </div>
  );
};

export default Alert;
