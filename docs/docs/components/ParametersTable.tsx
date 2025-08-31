import React from 'react';
import styles from './ParametersTable.module.css';

export interface Parameter {
  name: string;
  required?: boolean;
  type?: string;
  dataType?: string;
  description?: React.ReactNode;
}

interface ParametersTableProps {
  parameters?: Parameter[];
  className?: string;
}

const ParametersTable: React.FC<ParametersTableProps> = ({
  parameters = [],
  className = '',
}) => {
  return (
    <div className={`${styles.tableContainer} ${className}`}>
      <table className={styles.parametersTable}>
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {parameters.map((param, index) => (
            <tr key={param.name ? `${param.name}-${index}` : index}>
              <td>
                <div className={styles.parameterCell}>
                  <span className={styles.parameterName}>{param.name}</span>
                  {param.required && (
                    <span className={styles.parameterRequired}>required</span>
                  )}
                  {param.type && (
                    <div className={styles.parameterType}>{param.type}</div>
                  )}
                </div>
              </td>
              <td>
                <span className={styles.typeLabel}>{param.dataType || param.type}</span>
              </td>
              <td className={styles.parameterDescription}>
                {param.description}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ParametersTable;
